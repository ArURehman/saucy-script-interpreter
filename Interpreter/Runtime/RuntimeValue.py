from Interpreter.Runtime.ValueType import ValueType

class RuntimeValue:
    
    def __init__(self, kind: ValueType) -> None:
        self.kind = kind
        
    def __repr__(self) -> str:
        return f"{self.kind}"