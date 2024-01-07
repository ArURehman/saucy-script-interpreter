from Lexer.TokenType import TokenType

class Keyword:
    
    keywords = {
        'let': TokenType.LET,
        'func': TokenType.FUNC,
        'for': TokenType.FOR,
        'till': TokenType.TILL,
        'if': TokenType.IF,
        'elif': TokenType.ELIF,
        'else': TokenType.ELSE,
        'true': TokenType.BOOLEAN,
        'false': TokenType.BOOLEAN
    }