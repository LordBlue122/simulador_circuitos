from itertools import product


class TruthTableGenerator:

    def __init__(
        self,
        simulator,
        input_nodes,
        output_nodes
    ):
        self.simulator = simulator
        self.input_nodes = input_nodes
        self.output_nodes = output_nodes

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

            outputs = []

            for node in self.output_nodes:
                outputs.append(
                    node.evaluate()
                )

            row = {
                "inputs": list(values),
                "outputs": outputs
            }

            table.append(row)
            
            self.table = table

        return table
    
    def print_table(self):

        table = self.generate()

        for row in table:

            print(
                f"{row['inputs']} -> "
                f"{row['outputs']}"
            )