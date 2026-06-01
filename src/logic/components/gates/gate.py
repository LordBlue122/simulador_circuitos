from abc import ABC, abstractmethod


class Gate(ABC):

    def __init__(self, name: str, num_inputs: int):
        self.name = name
        self.num_inputs = num_inputs
        self.inputs = [False] * num_inputs
        self.output = False

    @abstractmethod
    def evaluate(self) -> bool:
        pass

    def set_input(self, index: int, value: bool) -> None:
        self.inputs[index] = value

    def get_output(self) -> bool:
        return self.output