#File for running the interpreter
from Lexer.Lexer import Lexer

lexer = Lexer('let x = 45*(5/2)')
tokens = lexer.tokenize()
for token in tokens:
    print(token)