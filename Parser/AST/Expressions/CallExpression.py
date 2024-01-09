from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class CallExpression(Expression):
    
    def __init__(self, arguments: list[Expression], calle: Expression) -> None:
        super().__init__(NodeType.CALL_EXPRESSION)
        self.arguments = arguments
        self.calle = calle
        
    def __repr__(self):
        return f"{self.calle}:{self.arguments}"