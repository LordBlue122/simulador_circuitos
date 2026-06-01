from collections import deque


class Simulator:

    def __init__(self, circuit):
        self.circuit = circuit

    def run(self):

        ordered_nodes = self._topological_sort()

        for component in ordered_nodes:

            if hasattr(component, "inputs"):
                component.evaluate()

            self._propagate(component)

    def _propagate(self, component):

        value = component.evaluate()

        for wire in self.circuit.get_wires():

            if wire.source != component:
                continue

            target = wire.target

            if hasattr(target, "inputs"):

                target.inputs[
                    wire.target_input_index
                ] = value

            elif hasattr(target, "set_value"):

                target.set_value(value)

    def _topological_sort(self):

        graph = {}
        indegree = {}

        for component in self.circuit.get_components():

            graph[component] = []
            indegree[component] = 0

        for wire in self.circuit.get_wires():

            graph[wire.source].append(
                wire.target
            )

            indegree[wire.target] += 1

        queue = deque()

        for node, degree in indegree.items():

            if degree == 0:
                queue.append(node)

        ordered = []

        while queue:

            node = queue.popleft()

            ordered.append(node)

            for neighbour in graph[node]:

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return ordered