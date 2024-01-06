from Lexer.TokenType import TokenType

class Token:
    
    def __init__(self, token_type: TokenType, value: str="") -> None:
        self.token_type = token_type
        self.value = value
        
    def __repr__(self) -> str:
        if self.value:
            return f"{self.value} -> {self.token_type}"
        return f"{self.token_type}"