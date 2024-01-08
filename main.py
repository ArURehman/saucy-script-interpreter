from Lexer.Lexer import Lexer
from Parser.Parser import Parser
from Interpreter.Interpreter import Interpreter
from Interpreter.Environment.SymbolTable import SymbolTable

from Interpreter.Runtime.Values.NumberValue import NumberValue
from Interpreter.Runtime.Values.BooleanValue import BooleanValue

# fileLines = ''
# with open(input('File > '), 'r') as iFile:
#     fileLines =  iFile.readlines()
# fileLines = ''.join(fileLines)

# Uncomment the above lines for Production 

fileLines = input('> ') # Only for Development

table = SymbolTable()

# ------------
table.declareVariable('x', NumberValue(3))
table.declareVariable('y', BooleanValue(True))
# ------------

lexer = Lexer(fileLines)
tokens = lexer.tokenize()
# print(tokens) 

parser = Parser(tokens)
program = parser.parse()
# print(program) 

interpreter = Interpreter()
result = interpreter.interpret(program, table)
print(result)