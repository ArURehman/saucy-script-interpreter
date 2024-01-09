from Interpreter.Runtime.ValueType import ValueType
from Interpreter.Runtime.RuntimeValue import RuntimeValue
from Interpreter.Runtime.FunctionCall import FunctionCall

class NativeFunctionValue(RuntimeValue):
    
    def __init__(self, call: FunctionCall) -> None:
        super().__init__(ValueType.NATIVE_FUNCTION)
        self.call = call
        
    def __repr__(self) -> str:
        return f"{ValueType.NATIVE_FUNCTION}:{self.call}"