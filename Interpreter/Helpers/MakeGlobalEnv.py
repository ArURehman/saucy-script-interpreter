from Interpreter.Environment.SymbolTable import SymbolTable
from Interpreter.Runtime.Values.NativeFunctionValue import NativeFunctionValue
from Interpreter.Runtime.FunctionCall import FunctionCall
from Interpreter.Runtime.ValueType import ValueType as VT

def printFunction(args, table):
    for arg in args:
        print(arg.value, end="")
    return FunctionCall(args, table)

def addFunction(args, table):
    result = 0
    for arg in args:
        if arg.kind == VT.NUMBER:
            result += arg.value
    print("\n", result)
    return FunctionCall(args, table)

def createGlobalEnv() -> SymbolTable:
    table = SymbolTable()
    table.declareVariable('print', NativeFunctionValue(printFunction))
    table.declareVariable('add', NativeFunctionValue(addFunction))
    return table