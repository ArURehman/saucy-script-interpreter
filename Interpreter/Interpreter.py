from Interpreter.Runtime.ValueType import ValueType as VT
from Interpreter.Runtime.RuntimeValue import RuntimeValue

from Interpreter.Runtime.Values.NullValue import NullValue
from Interpreter.Runtime.Values.NumberValue import NumberValue
from Interpreter.Runtime.Values.BooleanValue import BooleanValue
from Interpreter.Runtime.Values.ObjectValue import ObjectValue
from Interpreter.Runtime.Values.StringValue import StringValue
from Interpreter.Runtime.Values.FunctionValue import FunctionValue

from Interpreter.Environment.SymbolTable import SymbolTable

from Parser.AST.NodeType import NodeType as NT
from Parser.AST.Statement import Statement

from Parser.AST.Expressions.AssignmentExpression import AssignmentExpression

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
        
        if not (hasattr(left, 'kind') and hasattr(right, 'kind')):
            return NullValue()
        
        if left.kind == VT.NUMBER and right.kind == VT.NUMBER:
            return self.__makeCalculation(left.value, right.value, binaryOperation.operator.value)        
        
        return NullValue()
    
    # Evaluates to check existence of identifier and returns its value
    def __evaluateIdentifier(self, identifier: NT.IDENTIFIER, table: SymbolTable) -> RuntimeValue:
        result = table.lookupVariable(identifier)
        return result
    
    # Evaluates object literals 
    def __evaluateObject(self, obj: NT.OBJECT_LITERAL, table: SymbolTable) -> RuntimeValue:
        objectVal = ObjectValue({})
        
        for item in obj.properties:
            runtimeVal = self.__evaluate(item.value, table) if item.value else table.lookupVariable(item.key)
            objectVal.properties[item.key] = runtimeVal
        
        return objectVal
    
    # Handles calling functions
    def __callExpression(self, callExpr: NT.CALL_EXPRESSION, table: SymbolTable) -> RuntimeValue:
        args = []
        for arg in callExpr.arguments:
            args.append(self.__evaluate(arg, table))
        
        function = self.__evaluate(callExpr.caller, table)
        if function.kind == VT.NATIVE_FUNCTION:
            result = function.call(args, table)
            return result
        elif function.kind == VT.FUNCTION:
            scope = SymbolTable(function.table)
            for i in range(len(function.parameters)):
                if i > len(args):
                    raise Exception("Invalid Number of Arguments")
                var = function.parameters[i]
                arg = args[i]
                table.declareVariable(var, arg)
            result = NullValue()
            for stmt in function.body:
                result = self.__evaluate(stmt, scope)
            return result
                
        raise Exception(f'Specified function {function} does not exist')
        
    # Handles Function Declaration
    def __functionDeclaration(self, node: NT.FUNC_DECLARATION, table: SymbolTable) -> RuntimeValue:
        function = FunctionValue(
            node.funcName,
            node.parameters,
            node.body, 
            table
        )
        return table.declareVariable(node.funcName, function)
    
    # Handles variable declaration
    def __variableDeclaration(self, declaration: NT.VARIABLE_DECLARATION, table: SymbolTable) -> RuntimeValue:
        value = self.__evaluate(declaration.value, table) if declaration.value else NullValue()
        return table.declareVariable(declaration.identifier, value)
    
    # Handles variable assignment
    def __variableAssignment(self, node: AssignmentExpression, table: SymbolTable) -> RuntimeValue:
        if node.identifier.kind != NT.IDENTIFIER:
            raise Exception(f"Invalid Token: {node.identifier}")
        return table.assignVariable(node.identifier.string, self.__evaluate(node.value, table))
    
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
        elif kind == NT.STRING_LITERAL:
            return StringValue(node.value)
        elif kind == NT.OBJECT_LITERAL:
            return self.__evaluateObject(node, table)
        elif kind == NT.CALL_EXPRESSION:
            return self.__callExpression(node, table)
        elif kind == NT.NULL_LITERAL:
            return NullValue()
        elif kind == NT.ASSIGNMENT_EXPRESSION:
            return self.__variableAssignment(node, table)
        elif kind == NT.IDENTIFIER:
            return self.__evaluateIdentifier(node.string, table)
        elif kind == NT.BINARY_EXPRESSTION:
            return self.__binaryExpression(node, table)
        elif kind == NT.VARIABLE_DECLARATION:
            return self.__variableDeclaration(node, table)
        elif kind == NT.FUNC_DECLARATION:
            return self.__functionDeclaration(node, table)
        elif kind == NT.PROGRAM:
            return self.__program(node, table)
        else:
            return f"Illegal AST Node - {kind}"
    
    def interpret(self, program: Statement, table: SymbolTable) -> RuntimeValue:
        return self.__evaluate(program, table)
    