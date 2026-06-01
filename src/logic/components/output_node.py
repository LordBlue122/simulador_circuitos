from .component import Component


class OutputNode(Component):

    def __init__(self, name: str):
        super().__init__(name)

        self.value = False

    def set_value(self, value: bool):
        self.value = value

    def evaluate(self) -> bool:
        return self.value
    
    
# usage
# output = OutputNode("OUT")
# output.set_value(True)
# assert output.evaluate() is True