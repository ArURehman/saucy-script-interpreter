from Parser.AST.Statement import Statement
from Parser.AST.NodeType import NodeType

from typing import Optional

class FunctionDeclaration(Statement):
    
    def __init__(self, funcName: str, parameters: list[str], body: list[Statement]) -> None:
        super().__init__(NodeType.FUNC_DECLARATION)
        self.funcName = funcName    
        self.parameters = parameters
        self.body = body
        
    def __repr__(self) -> str:
        return "{\n" + f"{NodeType.FUNC_DECLARATION}:\n\t{self.parameters}\n\t{self.body}" + "\n}"