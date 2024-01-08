from Lexer.TokenType import TokenType
from Lexer.Keyword import Keyword
from Lexer.Token import Token
import re

class Lexer:
    
    def __init__(self, sourceCode: str) -> None:
        self.sourceCode = sourceCode
    
    def tokenize(self) -> list[Token]:
        tokens = []
        source_char = re.split("", self.sourceCode)
        
        while len(source_char) > 0:
            if source_char[0] == '(':
                tokens.append(Token(TokenType.LEFT_ROUND_PAREN, source_char.pop(0)))
            elif source_char[0] == ')':
                tokens.append(Token(TokenType.RIGHT_ROUND_PAREN, source_char.pop(0)))
            elif source_char[0] == '{':
                tokens.append(Token(TokenType.LEFT_CURLY_PAREN, source_char.pop(0)))
            elif source_char[0] == '}':
                tokens.append(Token(TokenType.RIGHT_CURLY_PAREN, source_char.pop(0)))
            elif source_char[0] == '+':
                tokens.append(Token(TokenType.PLUS, source_char.pop(0)))
            elif source_char[0] == '-':
                tokens.append(Token(TokenType.MINUS, source_char.pop(0)))
            elif source_char[0] == '*':
                tokens.append(Token(TokenType.MULTIPLY, source_char.pop(0)))
            elif source_char[0] == '/':
                tokens.append(Token(TokenType.DIVIDE, source_char.pop(0)))
            elif source_char[0] == '^':
                tokens.append(Token(TokenType.POWER, source_char.pop(0)))
            elif source_char[0] == '=':
                tokens.append(Token(TokenType.EQUALS, source_char.pop(0)))
            elif source_char[0] == '%':
                tokens.append(Token(TokenType.MODULUS, source_char.pop(0)))
            elif source_char[0] == ';':
                tokens.append(Token(TokenType.DELIMITER, source_char.pop(0)))
            elif source_char[0] in ['==', '<', '>', '!', '!=', '<=', '>=']:
                tokens.append(Token(TokenType.RELATIONAL_OPERATOR, source_char.pop(0)))
            else:
                if re.match(r'[0-9]', source_char[0]):
                    number = ""
                    dotCount = 0
                    while len(source_char) > 0 and re.match(r'[0-9.]', source_char[0]):
                        if dotCount == 1 and source_char[0] == '.':
                            raise SyntaxError
                            exit(1)
                        if source_char[0] == '.':
                            dotCount += 1
                        number += source_char.pop(0)
                    
                    if number.find('.'):
                        tokens.append(Token(TokenType.FLOAT, number))
                    else:
                        tokens.append(Token(TokenType.INT, number))
                    
                elif re.match(r'[a-zA-z_\"\']', source_char[0]):
                    string = ""
                    while len(source_char) > 0 and re.match(r'[\w\"\']', source_char[0]):
                        string += source_char.pop(0)
                    
                    keyword = Keyword.keywords.get(string, None)
                    if keyword:
                        tokens.append(Token(keyword, string))
                    elif string.count("'") > 0 or string.count('"'):
                        punc_1, punc_2, string = string[0], string[-1], string[1:-1]
                        tokens.append(Token(TokenType.PUNCTUATOR, punc_1))
                        tokens.append(Token(TokenType.STRING, string))
                        tokens.append(Token(TokenType.PUNCTUATOR, punc_2))
                    else:
                        tokens.append(Token(TokenType.IDENTIFIER, string))
                
                elif source_char[0] in [' ', '\n', '\t', '']:
                    source_char.pop(0)
                
                else:
                    raise Exception(f"Unrecognized Character: '{source_char[0]}'")
                    exit(1)
        
        tokens.append(Token(TokenType.EOF, "EOF"))             
        return tokens