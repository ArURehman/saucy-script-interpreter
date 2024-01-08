from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class AssignmentExpression(Expression):
    
    def __init__(self, identifier: Expression, value: Expression):
        super().__init__(NodeType.ASSIGNMENT_EXPRESSION)
        self.identifier = identifier
        self.value = value
        
    def __repr__(self):
        return "{" + f"{self.identifier}:{self.value}" "}"