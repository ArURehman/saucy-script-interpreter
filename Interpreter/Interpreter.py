from Interpreter.Runtime.ValueType import ValueType as VT
from Interpreter.Runtime.RuntimeValue import RuntimeValue

from Interpreter.Runtime.Values.NullValue import NullValue
from Interpreter.Runtime.Values.NumberValue import NumberValue
from Interpreter.Runtime.Values.BooleanValue import BooleanValue

from Interpreter.Environment.SymbolTable import SymbolTable

from Parser.AST.NodeType import NodeType as NT
from Parser.AST.Statement import Statement

from typing import Union

class Interpreter:
    
    # Makes arithematic calculations on given values
    def __makeCalculation(self, left: Union[int, float], right: Union[int, float], operator: str) -> NumberValue:
        if operator == '+':
            return NumberValue(left + right)
        elif operator == '-':
            return NumberValue(left - right)
        elif operator == '*':
            return NumberValue(left * right)
        elif operator == '/':
            try:
                return NumberValue(left / right)
            except ZeroDivisionError as err:
                print(err)
                exit(1)
        elif operator == '%':
            return NumberValue(left % right)
    
    # Evaluates binary expression
    def __binaryExpression(self, binaryOperation: NT.BINARY_EXPRESSTION, table: SymbolTable) -> RuntimeValue:
        left = self.__evaluate(binaryOperation.left, table)
        right = self.__evaluate(binaryOperation.right, table)
        
        if left.kind == VT.NUMBER and right.kind == VT.NUMBER:
            return self.__makeCalculation(left.value, right.value, binaryOperation.operator.value)        
        
        return NullValue()
    
    def __evaluateIdentifier(self, identifier: NT.IDENTIFIER, table: SymbolTable) -> RuntimeValue:
        result = table.lookupVariable(identifier)
        return result
    
    def __variableDeclaration(self, declaration: NT.VARIABLE_DECLARATION, table: SymbolTable) -> RuntimeValue:
        value = self.__evaluate(declaration.value, table) if declaration.value else NullValue()
        return table.declareVariable(declaration.identifier, value)
    
    # Runs each statement inside program 
    def __program(self, program: NT.PROGRAM, table: SymbolTable) -> RuntimeValue:
        lastEval = NullValue()
        for stmt in program.body:
            lastEval = self.__evaluate(stmt, table)
        return lastEval
    
    # Evaluates each statement according to it's type
    def __evaluate(self, node: Statement, table: SymbolTable) -> RuntimeValue:
        kind = node.kind
        
        if kind == NT.NUMERIC_LITERAL:
            return NumberValue(node.value)
        elif kind == NT.NULL_LITERAL:
            return NullValue()
        elif kind == NT.IDENTIFIER:
            return self.__evaluateIdentifier(node.string, table)
        elif kind == NT.BINARY_EXPRESSTION:
            return self.__binaryExpression(node, table)
        elif kind == NT.VARIABLE_DECLARATION:
            return self.__variableDeclaration(node, table)
        elif kind == NT.PROGRAM:
            return self.__program(node, table)
        else:
            return f"Illegal AST Node - {kind}"
    
    def interpret(self, program: Statement, table: SymbolTable) -> RuntimeValue:
        return self.__evaluate(program, table)
    