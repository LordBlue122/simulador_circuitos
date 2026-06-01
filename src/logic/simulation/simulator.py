class Simulator:

    def __init__(self, circuit):
        self.circuit = circuit

    def run(self):

        for wire in self.circuit.get_wires():

            source_value = wire.source.evaluate()

            if hasattr(wire.target, "inputs"):

                wire.target.inputs[
                    wire.target_input_index
                ] = source_value

        for component in self.circuit.get_components():

            component.evaluate()

        for wire in self.circuit.get_wires():

            if hasattr(wire.target, "set_value"):

                wire.target.set_value(
                    wire.source.evaluate()
                )