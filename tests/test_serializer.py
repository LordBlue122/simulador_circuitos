import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.circuits.circuit import Circuit

from src.logic.components.input_node import InputNode
from src.logic.components.output_node import OutputNode

from src.logic.components.gates.and_gate import AndGate

from src.persistence.serializer import CircuitSerializer


def test_serialize_deserialize_circuit():

    circuit = Circuit()

    a = InputNode("A")
    b = InputNode("B")

    gate = AndGate("AND_1")

    out = OutputNode("OUT")

    circuit.add_component(a)
    circuit.add_component(b)
    circuit.add_component(gate)
    circuit.add_component(out)

    circuit.connect(a, gate, 0)
    circuit.connect(b, gate, 1)
    circuit.connect(gate, out, 0)

    data = CircuitSerializer.serialize(circuit)

    new_circuit = CircuitSerializer.deserialize(data)

    assert len(new_circuit.get_components()) == 4

    assert len(new_circuit.get_wires()) == 3
    
def test_serialized_structure():

    circuit = Circuit()

    a = InputNode("A")
    b = InputNode("B")

    gate = AndGate("AND_1")

    out = OutputNode("OUT")

    circuit.add_component(a)
    circuit.add_component(b)
    circuit.add_component(gate)
    circuit.add_component(out)

    circuit.connect(a, gate, 0)
    circuit.connect(b, gate, 1)
    circuit.connect(gate, out, 0)

    data = CircuitSerializer.serialize(circuit)

    assert "components" in data
    assert "connections" in data

    assert len(data["components"]) == 4
    assert len(data["connections"]) == 3
    
def test_component_names_are_preserved():

    circuit = Circuit()

    a = InputNode("A")
    b = InputNode("B")

    gate = AndGate("AND_1")

    out = OutputNode("OUT")

    circuit.add_component(a)
    circuit.add_component(b)
    circuit.add_component(gate)
    circuit.add_component(out)

    data = CircuitSerializer.serialize(circuit)

    component_names = {
        component["name"]
        for component in data["components"]
    }

    assert component_names == {
        "A",
        "B",
        "AND_1",
        "OUT"
    }