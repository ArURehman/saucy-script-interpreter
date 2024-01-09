from Interpreter.Runtime.ValueType import ValueType
from Interpreter.Runtime.RuntimeValue import RuntimeValue

class StringValue(RuntimeValue):
    
    def __init__(self, value: str) -> None:
        super().__init__(ValueType.STRING)
        self.value = value
        
    def __repr__(self) -> str:
        return f"{ValueType.STRING}:{self.value}"