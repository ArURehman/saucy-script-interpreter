from enum import Enum, auto 

class TokenType(Enum):
    IDENTIFIER = auto()
    DELIMITER = auto()
    #Assignment Operator
    EQUALS = auto()
    
    #Data Types
    INT = auto()
    FLOAT = auto()
    STRING = auto()
    BOOLEAN = auto()
    
    #Arithematic Operator
    PLUS = auto()
    MINUS = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
    POWER = auto()
    MODULUS = auto()
    
    #Relational Operator
    RELATIONAL_OPERATOR = auto()
        
    #Literal
    LEFT_ROUND_PAREN = auto()
    RIGHT_ROUND_PAREN = auto()
    LEFT_CURLY_PAREN = auto()
    RIGHT_CURLY_PAREN = auto()
    PUNCTUATOR = auto()
    
    #Keywords
    LET = auto()
    FUNC = auto()
    FOR = auto()
    TILL = auto()
    IF = auto()
    ELIF = auto()
    ELSE = auto()
    
    EOF = auto()
