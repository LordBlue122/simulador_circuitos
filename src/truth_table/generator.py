from itertools import product


class TruthTableGenerator:

    def __init__(
        self,
        simulator,
        input_nodes,
        output_node
    ):
        self.simulator = simulator
        self.input_nodes = input_nodes
        self.output_node = output_node

    def generate(self):

        table = []

        combinations = product(
            [False, True],
            repeat=len(self.input_nodes)
        )

        for values in combinations:

            for node, value in zip(
                self.input_nodes,
                values
            ):
                node.set_value(value)

            self.simulator.run()

            row = {
                "inputs": list(values),
                "output": self.output_node.evaluate()
            }

            table.append(row)

        return table
    
    def print_table(self):
        for row in self.table:
            print(f"Inputs: {row['inputs']} -> Output: {row['output']}")