from Lexer.Lexer import Lexer
from Parser.Parser import Parser

# fileLines = ''
# with open(input('File > '), 'r') as iFile:
#     fileLines =  iFile.readlines()
# fileLines = ''.join(fileLines)

# Uncomment the above lines for Production 

fileLines = input('> ') # Only for Development

lexer = Lexer(fileLines)
tokens = lexer.tokenize()
# print(tokens) 

parser = Parser(tokens)
program = parser.parse()
print(program)