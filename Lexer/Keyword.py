from Lexer.TokenType import TokenType as TT

class Keyword:
    
    keywords = {
        'let': TT.LET,
        'func': TT.FUNC,
        'for': TT.FOR,
        'till': TT.TILL,
        'if': TT.IF,
        'elif': TT.ELIF,
        'else': TT.ELSE,
        'true': TT.BOOLEAN,
        'false': TT.BOOLEAN,
        'null': TT.NULL
    }