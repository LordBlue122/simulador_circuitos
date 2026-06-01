from .gate import Gate


class XorGate(Gate):

    def __init__(self):
        super().__init__("XOR", 2)

    def evaluate(self) -> bool:
        self.output = self.inputs[0] != self.inputs[1]
        return self.output