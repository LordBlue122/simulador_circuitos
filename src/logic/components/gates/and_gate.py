from .gate import Gate


class AndGate(Gate):

    def __init__(self):
        super().__init__("AND", 2)

    def evaluate(self) -> bool:
        self.output = all(self.inputs)
        return self.output