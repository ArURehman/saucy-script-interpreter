from enum import Enum, auto

class NodeType(Enum):
    
    PROGRAM = auto()
    
    #Statements
    STATEMENT = auto()
    NUMERIC_LITERAL = auto()
    IDENTIFIER = auto()
    FUNC_DECLARATION = auto()
    IF_ELSE_DECLAEARTION = auto()
    FOR_LOOP_DECLARATION = auto()
    WHILE_LOOP_DECLARATION = auto()
    END_LINE = auto()
    
    #Expressions
    EXPRESSION = auto()
    BINARY_EXPRESSTION = auto()
    UNARY_EXPRESSION = auto()
    
    