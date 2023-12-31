from enum import Enum, auto

class ValueType(Enum):
    
    NULL = auto()
    NUMBER = auto()
    BOOLEAN = auto()
    OBJECT = auto()
    STRING = auto()
    
    NATIVE_FUNCTION = auto()
    FUNCTION = auto()