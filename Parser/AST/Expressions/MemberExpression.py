from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

class MemberExpression(Expression):
    
    def __init__(self, obj: Expression, prop: Expression, computed: bool) -> None:
        super().__init__(NodeType.MEMBER_EXPRESSION)
        self.obj = obj
        self.prop = prop
        self.computed = computed
        
    def __repr__(self):
        return f"{self.obj}:{self.prop}:{self.computed}"