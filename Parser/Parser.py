from Parser.AST.Expression import Expression
from Parser.AST.Statement import Statement
from Parser.AST.Program import Program

from Parser.AST.Expressions.BinaryExpression import BinaryExpression
from Parser.AST.Expressions.Identifier import Identifier
from Parser.AST.Expressions.NumericLiteral import NumericLiteral
from Parser.AST.Expressions.NullLiteral import NullLiteral
from Parser.AST.Expressions.BooleanLiteral import BooleanLiteral
from Parser.AST.Expressions.AssignmentExpression import AssignmentExpression

from Parser.AST.Statements.VariableDeclaration import VariableDeclaration

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
    
    #Prcedence 2 (Used to Parse Multiplicative/Divisive/Modulus:% Expressions)
    def __scaleBinaryExpression(self) -> Expression:
        left = self.__primaryExpression()
        
        while self.__get().token_type in [TT.MULTIPLY, TT.DIVIDE, TT.MODULUS]:
            operator = self.__eat()
            right = self.__primaryExpression()
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
    
    def __assignmentExpression(self) -> Expression:
        leftExpr = self.__shiftBinaryExpression()
        
        if self.__get().token_type == TT.EQUALS:
            self.__eat()
            value = self.__assignmentExpression()
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
    
    # Calls parse function with lowest Precedence in the AST
    def __parseExpression(self) -> Expression:
        return self.__assignmentExpression()
    
    # Parses Statements first then expressions
    def __parseStatement(self) -> Statement:
        if self.__get().token_type == TT.LET:
            return self.__variableDeclaration()
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