from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType
from typing import Union

class NumericLiteral(Expression):
    
    def __init__(self, value: Union[int, float]):
        super().__init__(NodeType.NUMERIC_LITERAL)
        self.value = value
        
    def __repr__(self):
        return "{" + f"{NodeType.NUMERIC_LITERAL}:{self.value}" "}"