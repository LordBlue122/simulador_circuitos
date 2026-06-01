from src.logic.components.input_node import InputNode
from src.logic.components.output_node import OutputNode

from src.logic.components.gates.and_gate import AndGate
from src.logic.components.gates.or_gate import OrGate
from src.logic.components.gates.xor_gate import XorGate
from src.logic.components.gates.not_gate import NotGate

from src.logic.circuits.circuit import Circuit

class CircuitSerializer:

    COMPONENT_TYPES = {
        "InputNode": InputNode,
        "OutputNode": OutputNode,
        "AndGate": AndGate,
        "OrGate": OrGate,
        "XorGate": XorGate,
        "NotGate": NotGate
    }

    @classmethod
    def serialize(cls, circuit):

        data = {
            "components": [],
            "connections": []
        }

        for component in circuit.get_components():

            data["components"].append({
                "name": component.name,
                "type": component.__class__.__name__
            })

        for wire in circuit.get_wires():

            data["connections"].append({
                "source": wire.source.name,
                "target": wire.target.name,
                "input_index": wire.target_input_index
            })

        return data
    
    @classmethod
    def deserialize(cls, data):

        circuit = Circuit()

        components = {}

        for item in data["components"]:

            component_type = item["type"]
            name = item["name"]

            component_class = cls.COMPONENT_TYPES[
                component_type
            ]

            component = component_class(name)

            components[name] = component

            circuit.add_component(component)

        for connection in data["connections"]:

            source = components[
                connection["source"]
            ]

            target = components[
                connection["target"]
            ]

            circuit.connect(
                source,
                target,
                connection["input_index"]
            )

        return circuit