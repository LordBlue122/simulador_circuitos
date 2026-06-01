from .gate import Gate


class NotGate(Gate):

    def __init__(self):
        super().__init__("NOT", 1)

    def evaluate(self) -> bool:
        self.output = not self.inputs[0]
        return self.output