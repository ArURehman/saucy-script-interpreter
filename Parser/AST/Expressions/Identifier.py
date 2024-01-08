from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class Identifier(Expression):
    
    def __init__(self, string: str) -> None:
        super().__init__(NodeType.IDENTIFIER)
        self.string = string
        
    def __repr__(self): 
        return "{" + f"{NodeType.IDENTIFIER}:{self.string}" + "}"