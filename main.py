#File for running the interpreter
from Lexer.Lexer import Lexer
from Parser.Parser import Parser

fileLines = ''
with open('example.sc', 'r') as iFile:
    fileLines =  iFile.readlines()
fileLines = ''.join(fileLines)

lexer = Lexer(fileLines)
tokens = lexer.tokenize()

parser = Parser(tokens)
program = parser.parse()
print(program)