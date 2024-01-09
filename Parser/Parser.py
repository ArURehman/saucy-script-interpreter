from Parser.AST.Expression import Expression
from Parser.AST.Statement import Statement
from Parser.AST.Program import Program

from Parser.AST.NodeType import NodeType as NT

from Parser.AST.Expressions.BinaryExpression import BinaryExpression
from Parser.AST.Expressions.AssignmentExpression import AssignmentExpression
from Parser.AST.Expressions.MemberExpression import MemberExpression
from Parser.AST.Expressions.CallExpression import CallExpression

from Parser.AST.Literals.Identifier import Identifier
from Parser.AST.Literals.NumericLiteral import NumericLiteral
from Parser.AST.Literals.StringLiteral import StringLiteral
from Parser.AST.Literals.NullLiteral import NullLiteral
from Parser.AST.Literals.BooleanLiteral import BooleanLiteral
from Parser.AST.Literals.ObjectLiteral import ObjectLiteral
from Parser.AST.Literals.PropertyLiteral import PropertyLiteral

from Parser.AST.Statements.VariableDeclaration import VariableDeclaration
from Parser.AST.Statements.FunctionDeclaration import FunctionDeclaration

from Lexer.Token import Token
from Lexer.TokenType import TokenType as TT

class Parser:
    
    def __init__(self, tokens: list[Token]=[TT.EOF]) -> None:
        self.tokens = tokens
        
    def __endOfFile(self) -> bool:
        return self.tokens[0].token_type == TT.EOF
    
    def __get(self) -> Token:
        return self.tokens[0]
    
    def __eat(self) -> Token:
        return self.tokens.pop(0)
    
    def __expect(self, tokenType: TT, error: str) -> Token:
        token = self.__eat()
        if not token or token.token_type != tokenType:
            raise Exception(f"Error: {error} - Token: {token} - Expected: {tokenType}")
            exit(1)
        return token
    
    #Highest Precedence
    def __primaryExpression(self) -> Expression:
        token = self.__get()
        
        if token.token_type == TT.IDENTIFIER:
            return Identifier(self.__eat().value)
        elif token.token_type == TT.PUNCTUATOR:
            self.__eat()
            value = StringLiteral(self.__eat().value)
            self.__expect(TT.PUNCTUATOR, "Unexpected Token")
            return value
        elif token.token_type == TT.NULL:
            self.__eat()
            return NullLiteral()
        elif token.token_type == TT.BOOLEAN:
            return BooleanLiteral(self.__eat().value)
        elif token.token_type == TT.INT:
            return NumericLiteral(int(self.__eat().value))
        elif token.token_type == TT.FLOAT:
            return NumericLiteral(float(self.__eat().value))
        elif token.token_type == TT.LEFT_ROUND_PAREN:
            self.__eat()
            value = self.__parseExpression()
            self.__expect(TT.RIGHT_ROUND_PAREN, 'Unexpected Token')
            return value 
        else:
            raise Exception(f"Unexpected Token: {token}")
            exit(1)
            
    def __memberExpression(self) -> Expression:
        obj = self.__primaryExpression()
        
        while self.__get().token_type in [TT.DOT, TT.LEFT_BRACKET] :
            operator = self.__eat()
            prop = None
            computed = False
            if operator.token_type == TT.DOT:
                computed = False                
                prop = self.__primaryExpression()
                if prop.kind != NT.IDENTIFIER and prop.kind != NT.STRING_LITERAL:
                    raise Exception("Syntax Error: Identifier Not Detected")
            else:
                computed = True
                prop = self.__parseExpression()
                self.__expect(TT.RIGHT_BRACKET, "Missing Token")
            
            obj = MemberExpression(obj, prop, computed)
                    
        return obj
    
    def __callExpression(self, caller: Expression) -> Expression:
        callExpr = CallExpression(caller, self.__parseArguments())
        if self.__get().token_type == TT.LEFT_ROUND_PAREN:
            callExpr = self.__callExpression(callExpr)
        return callExpr
    
    # Handles call and member expressions recursively
    def __callMemberExpression(self) -> Expression:
        member = self.__memberExpression()
        if self.__get().token_type == TT.LEFT_ROUND_PAREN:
            return self.__callExpression(member)
        return member
    
    # Parses arguments
    def __parseArguments(self) -> list[Expression]:
        self.__expect(TT.LEFT_ROUND_PAREN, "Missing Token")
        args = [] if self.__get().token_type == TT.RIGHT_ROUND_PAREN else self.__parseArgumentList()
        self.__expect(TT.RIGHT_ROUND_PAREN, "Missing Token")
        return args
    
    def __parseArgumentList(self) -> list[Expression]:
        args = [self.__assignmentExpression()]
        while self.__get().token_type == TT.COMMA and self.__eat():
            args.append(self.__assignmentExpression())
        return args
    
    #Prcedence 2 (Used to Parse Multiplicative/Divisive/Modulus:% Expressions)
    def __scaleBinaryExpression(self) -> Expression:
        left = self.__callMemberExpression()
        
        while self.__get().token_type in [TT.MULTIPLY, TT.DIVIDE, TT.MODULUS]:
            operator = self.__eat()
            right = self.__callMemberExpression()
            left = BinaryExpression(left, right, operator)
        
        return left
    
    #Prcedence 2 (Used to Parse Additive/Subtractive Expressions)
    def __shiftBinaryExpression(self) -> Expression:
        left = self.__scaleBinaryExpression()
        
        while self.__get().token_type in [TT.PLUS, TT.MINUS]:
            operator = self.__eat()
            right = self.__scaleBinaryExpression()
            left = BinaryExpression(left, right, operator)
        
        return left
    
    # Handles Object Assignment {key:value}
    def __objectAssignment(self) -> Expression:
        if self.__get().token_type != TT.LEFT_CURLY_PAREN:
            return self.__shiftBinaryExpression()
        
        self.__eat()
        properties = []
        
        while not self.__endOfFile() and self.__get().token_type != TT.RIGHT_CURLY_PAREN:
            key = self.__expect(TT.IDENTIFIER, "Unexpected Token").value
            
            if self.__get().token_type == TT.COMMA: # Case: {key,}
                self.__eat()
                properties.append(PropertyLiteral(key))
                continue
            elif self.__get().token_type == TT.RIGHT_CURLY_PAREN: # Case: {key}
                properties.append(PropertyLiteral(key))
                continue
            
            self.__expect(TT.COLON, "Missing Token") # Case: {key:value}
            value = self.__parseExpression()
            properties.append(PropertyLiteral(key, value))
            if self.__get().token_type != TT.RIGHT_CURLY_PAREN:
                self.__expect(TT.COMMA, "Missing Token")
                
        
        self.__expect(TT.RIGHT_CURLY_PAREN, "Missing Token")
        return ObjectLiteral(properties)
    
    # Handles value assignment to variables (Doesn't declare them)
    def __assignmentExpression(self) -> Expression:
        leftExpr = self.__objectAssignment()
        
        if self.__get().token_type == TT.DELIMITER:
            self.__eat()
        
        if self.__get().token_type == TT.EQUALS:
            self.__eat()
            value = self.__assignmentExpression()
            if self.__get().token_type == TT.DELIMITER:
                self.__eat()
            return AssignmentExpression(leftExpr, value)
        
        return leftExpr
    
    # Parses variable declaration statements 
    def __variableDeclaration(self) -> Statement:
        let = self.__expect(TT.LET, "Unexpected Token").value 
        identifier = self.__expect(TT.IDENTIFIER, "Unexpected Token").value
        
        if self.__get().token_type == TT.DELIMITER:
            self.__eat()
            return VariableDeclaration(identifier)
        
        self.__expect(TT.EQUALS, "Unexpected Token")

        declaration = VariableDeclaration(identifier, self.__parseExpression())
        return declaration
    
    # TODO: Add if-else expression support
    
    def __functionDeclaration(self) -> Statement:
        self.__eat()
        funcName = self.__expect(TT.IDENTIFIER, "Missing Token Function Name").value
        
        args = self.__parseArguments()
        params = []
        for arg in args:
            if arg.kind != NT.IDENTIFIER:
                raise Exception("Parameters Expected In Function Declaration")
            params.append(arg.string)
        self.__expect(TT.LEFT_CURLY_PAREN, "Missing Token 'Opening Curly Brace'")
        
        body = []
        while self.__get().token_type not in [TT.EOF, TT.RIGHT_CURLY_PAREN]:
            body.append(self.__parseStatement())
        self.__expect(TT.RIGHT_CURLY_PAREN, "Missing Token 'Closing Curly Brace'")
        
        return FunctionDeclaration(funcName, params, body)
    
    # Calls parse function with lowest Precedence in the AST
    def __parseExpression(self) -> Expression:
        return self.__assignmentExpression()
    
    # Parses Statements first then expressions
    def __parseStatement(self) -> Statement:
        if self.__get().token_type == TT.LET:
            return self.__variableDeclaration()
        elif self.__get().token_type == TT.FUNC:
            return self.__functionDeclaration()
        else:
            return self.__parseExpression()
        
    # Moves through each expression/statement in AST and gets it parsed
    def __produceAST(self) -> Program:
        program = Program([])
        
        while not self.__endOfFile():
            program.body.append(self.__parseStatement())
        
        return program    
    
    def parse(self) -> Program:
        return self.__produceAST()