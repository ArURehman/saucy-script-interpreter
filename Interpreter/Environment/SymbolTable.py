from __future__ import annotations
from typing import Optional

from Interpreter.Runtime.RuntimeValue import RuntimeValue


class SymbolTable:
    
    def __init__(self, parent: Optional[SymbolTable]=None) -> None:
        self.parent = parent
        self.globals = True if parent else False
        self.variables = {}
        
    def declareVariable(self, variableName: str, value: RuntimeValue) -> RuntimeValue:
        if self.variables.get(variableName, None):
            raise Exception(f"Declaration Error: Cannot declare already declared variable '{variableName}:{value}'")
        
        self.variables[variableName] = value
        return value
    
    def resolveVariable(self, variableName: str) -> SymbolTable:
        if self.variables.get(variableName, None):
            return self
        
        if self.parent is None:
            raise Exception(f"Resolution Error: Couldn't resolve variable '{variableName}'")
        
        return self.parent.resolveVariable(variableName)
    
    def assignVariable(self, variableName: str, value: RuntimeValue) -> RuntimeValue:
        table = self.resolveVariable(variableName)
        table.variables[variableName] = value
        return value
    
    def lookupVariable(self, variableName: str) -> RuntimeValue:
        table = self.resolveVariable(variableName)
        return table.variables.get(variableName)