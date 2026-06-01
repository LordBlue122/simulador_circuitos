from .gate import Gate


class NotGate(Gate):

    def __init__(self, name: str):
        super().__init__(name, 1)

    def evaluate(self) -> bool:
        self.output = not self.inputs[0]
        return self.output