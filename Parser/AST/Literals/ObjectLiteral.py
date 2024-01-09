from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

from Parser.AST.Literals.PropertyLiteral import PropertyLiteral as Property

class ObjectLiteral(Expression):
    
    def __init__(self, properties: list[Property]):
        super().__init__(NodeType.OBJECT_LITERAL)
        self.properties = properties
        
    def __repr__(self):
        return "{" + f"{NodeType.OBJECT_LITERAL}:{self.properties}" "}"