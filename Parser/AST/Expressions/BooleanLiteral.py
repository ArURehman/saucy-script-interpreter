from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class BooleanLiteral(Expression):
    
    def __init__(self, value: bool):
        super().__init__(NodeType.BOOLEAN_LITERAL)
        self.value = value
        
    def __repr__(self):
        return "{" + f"{NodeType.BOOLEAN_LITERAL}:{self.value}" "}"