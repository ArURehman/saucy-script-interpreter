from Parser.AST.NodeType import NodeType
from Lexer.Token import Token

class EndLineNode:
    
    def __init__(self, token: Token) -> None:
        self.node = token
        self.type = NodeType.END_LINE
        
    def __repr__(self) -> str:
        return f"{self.node}"