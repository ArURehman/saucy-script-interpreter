from Parser.AST.NodeType import NodeType
from Lexer.Token import Token

class BinaryOperationNode: 
    
    def __init__(self, left_node: Token, operator: Token, right_node: Token):
        self.left_node = left_node
        self.operator = operator
        self.right_node = right_node
        self.type = NodeType.BINARY_EXPRESSTION
        
    def __repr__(self) -> str:
        return f"({self.left_node} : {self.operator} : {self.right_node})"