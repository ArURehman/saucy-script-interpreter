from Interpreter.Runtime.ValueType import ValueType
from Interpreter.Runtime.RuntimeValue import RuntimeValue
from typing import Union

class NumberValue(RuntimeValue):
    
    def __init__(self, value: Union[int, float]) -> None:
        super().__init__(ValueType.NUMBER)
        self.value = value
        
    def __repr__(self) -> str:
        return f"{ValueType.NUMBER}:{self.value}"