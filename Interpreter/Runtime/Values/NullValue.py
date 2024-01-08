from Interpreter.Runtime.ValueType import ValueType
from Interpreter.Runtime.RuntimeValue import RuntimeValue

class NullValue(RuntimeValue):
    
    def __init__(self, value: str=None) -> None:
        super().__init__(ValueType.NULL)
        self.value = value
        
    def __repr__(self) -> str:
        return f"{ValueType.NULL}:{self.value}"