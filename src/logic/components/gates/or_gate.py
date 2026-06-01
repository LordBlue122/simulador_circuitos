from .gate import Gate


class OrGate(Gate):

    def __init__(self):
        super().__init__("OR", 2)

    def evaluate(self) -> bool:
        self.output = any(self.inputs)
        return self.output