from Interpreter.Environment.SymbolTable import SymbolTable
from Interpreter.Runtime.RuntimeValue import RuntimeValue

class FunctionCall:
    
    def __init__(self, args: list[RuntimeValue], table: SymbolTable) -> None:
        self.args = args
        self.table = table
        
    def __repr__(self) -> str:
        return f"{self.args}:{self.table}"
