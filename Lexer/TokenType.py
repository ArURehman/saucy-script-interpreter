from enum import Enum, auto 

class TokenType(Enum):
    NUMBER = auto()
    IDENTIFIER = auto()
    
    #Assignment Operator
    EQUALS = auto()
    
    #Arithematic Operator
    BINARY_OPERATOR = auto()
    
    #Relational Operator
    RELATIONAL_OPERATOR = auto()
    
    #Literal
    LEFT_ROUND_PAREN = auto()
    RIGHT_ROUND_PAREN = auto()
    LEFT_CURLY_PAREN = auto()
    RIGHT_CURLY_PAREN = auto()
    
    #Keywords
    LET = auto()
    FUNC = auto()
    FOR = auto()
    TILL = auto()
    IF = auto()
    ELIF = auto()
    ELSE = auto()
    
    EOF = auto()

