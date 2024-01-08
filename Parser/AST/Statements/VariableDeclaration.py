from Parser.AST.Statement import Statement
from Parser.AST.Expression import Expression
from Parser.AST.NodeType import NodeType

from typing import Optional

class VariableDeclaration(Statement):
    
    def __init__(self, identifier: str, value: Optional[Expression]=None) -> None:
        super().__init__(NodeType.VARIABLE_DECLARATION)
        self.identifier = identifier
        self.value = value
        
    def __repr__(self) -> str:
        return "{\n" + f"{NodeType.VARIABLE_DECLARATION}:\n\t{self.identifier}\n\t{self.value}" + "\n}"