from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class NullLiteral(Expression):
    
    def __init__(self, value: str='null'):
        super().__init__(NodeType.NULL_LITERAL)
        self.value = value
        
    def __repr__(self):
        return "{" + f"{NodeType.NULL_LITERAL}:{self.value}" "}"