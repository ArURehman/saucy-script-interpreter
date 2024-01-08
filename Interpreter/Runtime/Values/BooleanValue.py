from Interpreter.Runtime.ValueType import ValueType
from Interpreter.Runtime.RuntimeValue import RuntimeValue

class BooleanValue(RuntimeValue):
    
    def __init__(self, value: bool) -> None:
        super().__init__(ValueType.BOOLEAN)
        self.value = value
        
    def __repr__(self) -> str:
        return f"{ValueType.BOOLEAN}:{self.value}"