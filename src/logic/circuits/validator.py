class CircuitValidator:

    def __init__(self, circuit):
        self.circuit = circuit

    def validate(self) -> bool:
        return (
            self.validate_self_connections()
            and self.validate_input_indexes()
            and self.validate_duplicate_inputs()
            and self.validate_acyclic()
        )

    def validate_self_connections(self) -> bool:

        for wire in self.circuit.get_wires():

            if wire.source == wire.target:
                return False

        return True

    def validate_input_indexes(self) -> bool:

        for wire in self.circuit.get_wires():

            target = wire.target

            if hasattr(target, "inputs"):

                if (
                    wire.target_input_index < 0
                    or wire.target_input_index >= len(target.inputs)
                ):
                    return False

        return True

    def validate_duplicate_inputs(self) -> bool:

        used_inputs = set()

        for wire in self.circuit.get_wires():

            target = wire.target

            if hasattr(target, "inputs"):

                key = (
                    id(target),
                    wire.target_input_index
                )

                if key in used_inputs:
                    return False

                used_inputs.add(key)

        return True

    def validate_acyclic(self) -> bool:

        graph = self._build_graph()

        visited = set()
        recursion_stack = set()

        for node in graph:

            if node not in visited:

                if self._has_cycle(
                    node,
                    graph,
                    visited,
                    recursion_stack
                ):
                    return False

        return True

    def _build_graph(self):

        graph = {}

        for component in self.circuit.get_components():
            graph[component] = []

        for wire in self.circuit.get_wires():

            source = wire.source
            target = wire.target

            if source not in graph:
                graph[source] = []

            graph[source].append(target)

        return graph

    def _has_cycle(
        self,
        node,
        graph,
        visited,
        recursion_stack
    ):

        visited.add(node)
        recursion_stack.add(node)

        for neighbour in graph.get(node, []):

            if neighbour not in visited:

                if self._has_cycle(
                    neighbour,
                    graph,
                    visited,
                    recursion_stack
                ):
                    return True

            elif neighbour in recursion_stack:
                return True

        recursion_stack.remove(node)

        return False
    
    def would_create_cycle(
            self,
            source,
            target
        ):

        graph = self._build_graph()

        return self._path_exists(
            start=target,
            goal=source,
            graph=graph
        )