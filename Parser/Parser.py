from Lexer.Token import Token
from Lexer.TokenType import TokenType as TT
from Parser.AST.NumericLiteral import NumericLiteralNode
from Parser.AST.BinaryOperation import BinaryOperationNode
from Parser.AST.EndLine import EndLineNode

class Parser:
    
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.index = 0
        self.__advance()
        
    def __advance(self) -> Token:
        if self.index < len(self.tokens):
            self.currToken = self.tokens[self.index]
        self.index += 1
        return self.currToken
    
    def __factor(self) -> NumericLiteralNode:
        token = self.currToken
        if token.token_type in [TT.INT, TT.FLOAT]:
            self.__advance()
            return NumericLiteralNode(token)
    
    def __term(self) -> BinaryOperationNode:
        return self.__binaryOperation(self.__factor, [TT.MULTIPLY, TT.DIVIDE])
    
    def __expr(self):
        return self.__binaryOperation(self.__term, [TT.PLUS, TT.MINUS])
    
    def __binaryOperation(self, function, operators: list[TT]) -> BinaryOperationNode:
        left_node = function()
        
        while self.currToken.token_type in operators:
            operator = self.currToken
            self.__advance()
            right_node = function()
            left_node = BinaryOperationNode(left_node, operator, right_node)
        
        return left_node
    
    def __endOfLine(self) -> EndLineNode:
        self.__advance()
        if self.currToken.token_type == TT.DELIMITER:
            return EndLineNode(self.currToken) 
    
    def parse(self):
        result = self.__expr()
        # result += self.__endOfLine()
        print(result)
        return result