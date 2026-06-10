from .wire import Wire


class Circuit:

    def __init__(self):
        self.components = []
        self.wires = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):

        if component in self.components:
            self.components.remove(component)

    def connect(
        self,
        source,
        target,
        target_input_index
    ):

        wire = Wire(
            source,
            target,
            target_input_index
        )

        self.wires.append(wire)

        return wire

    def get_components(self):
        return self.components

    def get_wires(self):
        return self.wires
    
    def is_input_connected(
        self,
        target,
        target_input_index
    ):

        for wire in self.wires:

            if (
                wire.target == target
                and
                wire.target_input_index == target_input_index
            ):
                return True

        return False