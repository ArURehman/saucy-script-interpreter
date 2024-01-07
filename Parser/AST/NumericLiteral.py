from Parser.AST.NodeType import NodeType
from Lexer.Token import Token

class NumericLiteralNode:
    
    def __init__(self, token: Token):
        self.node = token
        self.type = NodeType.NUMERIC_LITERAL
        
    def __repr__(self):
        return f"{self.node}"