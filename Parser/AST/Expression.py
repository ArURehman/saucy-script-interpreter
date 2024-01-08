from Parser.AST.Statement import Statement
from Parser.AST.NodeType import NodeType

class Expression(Statement):
    
    def __init__(self, kind: NodeType):
        super().__init__(kind)