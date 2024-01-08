from Parser.AST.Statement import Statement
from Parser.AST.NodeType import NodeType

class Program(Statement):
    
    def __init__(self, body: list[Statement]=[]) -> None:
        super().__init__(NodeType.PROGRAM)
        self.body = body
        
    def __repr__(self) -> str:
        return "{\n" + f"{NodeType.PROGRAM}:\n\t{self.body}" + "\n}"