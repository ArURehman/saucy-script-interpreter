from Interpreter.Runtime.ValueType import ValueType as VT
from Interpreter.Runtime.RuntimeValue import RuntimeValue

from Interpreter.Runtime.Values.NullValue import NullValue
from Interpreter.Runtime.Values.NumberValue import NumberValue

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
    def __binaryExpression(self, binaryOperation: NT.BINARY_EXPRESSTION) -> RuntimeValue:
        left = self.__evaluate(binaryOperation.left)
        right = self.__evaluate(binaryOperation.right)
        
        if left.kind == VT.NUMBER and right.kind == VT.NUMBER:
            return self.__makeCalculation(left.value, right.value, binaryOperation.operator.value)        
        
        return NullValue()
    
    # Runs each statement inside program 
    def __program(self, program: NT.PROGRAM) -> RuntimeValue:
        lastEval = NullValue()
        for stmt in program.body:
            lastEval = self.__evaluate(stmt)
        return lastEval
    
    # Evaluates each statement according to it's type
    def __evaluate(self, node: Statement) -> RuntimeValue:
        kind = node.kind
        
        if kind == NT.NUMERIC_LITERAL:
            return NumberValue(node.value)
        elif kind == NT.NULL_LITERAL:
            return NullValue()
        elif kind == NT.BINARY_EXPRESSTION:
            return self.__binaryExpression(node)
        elif kind == NT.PROGRAM:
            return self.__program(node)
        else:
            return f"Illegal AST Node - {kind}"
    
    def interpret(self, program: Statement) -> RuntimeValue:
        return self.__evaluate(program)
    