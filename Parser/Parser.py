from Parser.AST.Expression import Expression
from Parser.AST.Statement import Statement
from Parser.AST.Program import Program

from Parser.AST.Expressions.BinaryExpression import BinaryExpression
from Parser.AST.Expressions.Identifier import Identifier
from Parser.AST.Expressions.NumericLiteral import NumericLiteral

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
            raise Exception(f"Error: {error} - Expected: {tokenType}")
            exit(1)
        return token
    
    #Highest Precedence
    def __primaryExpression(self) -> Expression:
        token = self.__get()
        
        if token.token_type == TT.IDENTIFIER:
            return Identifier(self.__eat().value)
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
    
    #Calls parse function with lowest Precedence in the AST
    def __parseExpression(self) -> Expression:
        return self.__shiftBinaryExpression()
    
    def __parseStatement(self) -> Statement:
        #placeholder for statements to be added in future
        return self.__parseExpression()
        
    def __produceAST(self) -> Program:
        program = Program([])
        
        while not self.__endOfFile():
            program.body.append(self.__parseStatement())
        
        return program    
    
    def parse(self) -> Program:
        return self.__produceAST()