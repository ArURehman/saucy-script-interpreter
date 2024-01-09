from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class BinaryExpression(Expression):
    
    def __init__(self, obj: Expression, propert: Expression, computed: bool) -> None:
        super().__init__(NodeType.MEMBER_EXPRESSION)
        self.obj = obj
        self.propert = propert
        self.computed = computed
        
    def __repr__(self):
        return f""