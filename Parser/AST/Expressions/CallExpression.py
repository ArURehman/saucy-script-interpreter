from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class CallExpression(Expression):
    
    def __init__(self, caller: Expression, arguments: list[Expression]) -> None:
        super().__init__(NodeType.CALL_EXPRESSION)
        self.caller = caller
        self.arguments = arguments
        
    def __repr__(self):
        return f"{self.calle}:{self.arguments}"