from Parser.AST.NodeType import NodeType

class Statement:
    
    def __init__(self, kind: NodeType):
        self.kind = kind
        
    def __repr__(self):
        return f"{self.kind}"
    
