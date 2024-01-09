from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

from typing import Optional

class PropertyLiteral(Expression):
    
    def __init__(self, key: str, value: Optional[Expression]=None) -> None:
        super().__init__(NodeType.PROPERTY_LITERAL)
        self.key = key
        self.value = value 
        
    def __repr__(self):
        return "{" + f"{self.key}:{self.value}" "}"