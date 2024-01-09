from Lexer.Lexer import Lexer
from Parser.Parser import Parser
from Interpreter.Interpreter import Interpreter

from Interpreter.Environment.SymbolTable import SymbolTable
from Interpreter.Helpers.MakeGlobalEnv import createGlobalEnv

fileLines = ''
with open('Examples/funcExample.txt', 'r') as iFile:
    fileLines =  iFile.readlines()
fileLines = ''.join(fileLines)

table = createGlobalEnv() # Contains function declarations

lexer = Lexer(fileLines)
tokens = lexer.tokenize()

parser = Parser(tokens)
program = parser.parse()

interpreter = Interpreter()
result = interpreter.interpret(program, table)
# print(result)