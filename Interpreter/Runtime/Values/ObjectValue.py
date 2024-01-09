from Interpreter.Runtime.ValueType import ValueType
from Interpreter.Runtime.RuntimeValue import RuntimeValue

from typing import Union

class ObjectValue(RuntimeValue):
    
    def __init__(self, properties: dict[Union[str, RuntimeValue]]) -> None:
        super().__init__(ValueType.OBJECT)
        self.properties = properties
        
    def __repr__(self) -> str:
        return f"{ValueType.OBJECT}:{self.value}"