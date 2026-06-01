from .component import Component


class InputNode(Component):

    def __init__(
        self,
        name: str,
        value: bool = False
    ):
        super().__init__(name)

        self.value = value

    def set_value(self, value: bool):
        self.value = value

    def evaluate(self) -> bool:
        return self.value
    
    
# Usage
# input_a = InputNode("A")
#input_a.set_value(True)
#result = input_a.evaluate()
#assert result is True