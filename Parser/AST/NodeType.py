from enum import Enum, auto

class NodeType(Enum):
    
    PROGRAM = auto()
    
    #Statements
    STATEMENT = auto()
    
    VARIABLE_DECLARATION = auto()
    FUNC_DECLARATION = auto()
    IF_ELSE_DECLAEARTION = auto()
    FOR_LOOP_DECLARATION = auto()
    WHILE_LOOP_DECLARATION = auto()
    END_LINE = auto()
    
    #Expressions
    EXPRESSION = auto()
    MEMBER_EXPRESSION = auto()
    CALL_EXPRESSION = auto()
    
    #Literals
    PROPERTY_LITERAL = auto()
    OBJECT_LITERAL = auto()
    NUMERIC_LITERAL = auto()
    STRING_LITERAL = auto()
    NULL_LITERAL = auto()
    IDENTIFIER = auto()
    BOOLEAN_LITERAL = auto()
    
    BINARY_EXPRESSTION = auto()
    ASSIGNMENT_EXPRESSION = auto()
    UNARY_EXPRESSION = auto()
    