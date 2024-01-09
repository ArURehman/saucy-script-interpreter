from Interpreter.Environment.SymbolTable import SymbolTable
from Interpreter.Runtime.Values.NativeFunctionValue import NativeFunctionValue
from Interpreter.Runtime.FunctionCall import FunctionCall
from Interpreter.Runtime.ValueType import ValueType as VT

from Interpreter.Runtime.Values.NumberValue import NumberValue

def printFunction(args, table):
    for arg in args:
        print(arg.value, end="")
    print('\n')
    return FunctionCall(args, table)

def addFunction(args, table):
    result = 0
    for arg in args:
        if arg.kind == VT.NUMBER:
            result += arg.value
    return NumberValue(result)

def createGlobalEnv() -> SymbolTable:
    table = SymbolTable()
    table.declareVariable('print', NativeFunctionValue(printFunction))
    table.declareVariable('add', NativeFunctionValue(addFunction))
    return table