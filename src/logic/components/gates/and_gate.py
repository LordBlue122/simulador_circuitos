from .gate import Gate


class AndGate(Gate):

    def __init__(self, name: str):
        super().__init__(name, 2)

    def evaluate(self) -> bool:
        self.output = self.inputs[0] and self.inputs[1]
        return self.output