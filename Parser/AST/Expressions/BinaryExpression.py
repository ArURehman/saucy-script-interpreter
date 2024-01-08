from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class BinaryExpression(Expression):
    
    def __init__(self, left: Expression, right: Expression, operator: str) -> None:
        super().__init__(NodeType.BINARY_EXPRESSTION)
        self.left = left
        self.right = right
        self.operator = operator
        
    def __repr__(self):
        return f"\n\t\t{self.left}\n\t\t{self.operator}\n\t\t{self.right}\n\t"