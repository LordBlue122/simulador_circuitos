from abc import ABC


class Component(ABC):

    def __init__(self, name: str):
        self.name = name