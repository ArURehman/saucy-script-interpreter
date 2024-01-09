from Interpreter.Environment.SymbolTable import SymbolTable
from Interpreter.Runtime.Values.NativeFunctionValue import NativeFunctionValue
from Interpreter.Runtime.FunctionCall import FunctionCall
from Interpreter.Runtime.ValueType import ValueType as VT

def printFunction(args, table):
    for arg in args:
        if arg.kind == VT.NUMBER:
            print(arg.value)
    return FunctionCall(args, table)

def createGlobalEnv() -> SymbolTable:
    table = SymbolTable()
    table.declareVariable('print', NativeFunctionValue(printFunction))
    return table