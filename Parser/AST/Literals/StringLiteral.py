from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class StringLiteral(Expression):
    
    def __init__(self, value: str) -> None:
        super().__init__(NodeType.STRING_LITERAL)
        self.value = value
        
    def __repr__(self) -> str:
        return "{" + f"{NodeType.STRING_LITERAL}:{self.value}" "}"