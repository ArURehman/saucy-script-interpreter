from Interpreter.Runtime.ValueType import ValueType
from Interpreter.Runtime.RuntimeValue import RuntimeValue

from Parser.AST.Statement import Statement
from Interpreter.Environment.SymbolTable import SymbolTable

class FunctionValue(RuntimeValue):
    
    def __init__(self, funcName: str, parameters: list[str], body: list[Statement], table: SymbolTable) -> None:
        super().__init__(ValueType.FUNCTION)
        self.funcName = funcName
        self.parameters = parameters
        self.body = body
        self.table = table
        
    def __repr__(self) -> str:
        return f"{ValueType.FUNCTION}:{self.funcName}"