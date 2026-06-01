import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.circuits.circuit import Circuit

from src.logic.components.input_node import InputNode
from src.logic.components.output_node import OutputNode

from src.logic.components.gates.xor_gate import XorGate

from src.logic.simulation.simulator import Simulator

from src.truth_table.generator import TruthTableGenerator

from src.persistence.serializer import CircuitSerializer


def test_complete_workflow():

    circuit = Circuit()

    a = InputNode("A")
    b = InputNode("B")

    xor_gate = XorGate("XOR_1")

    out = OutputNode("OUT")

    circuit.add_component(a)
    circuit.add_component(b)
    circuit.add_component(xor_gate)
    circuit.add_component(out)

    circuit.connect(a, xor_gate, 0)
    circuit.connect(b, xor_gate, 1)

    circuit.connect(xor_gate, out, 0)

    simulator = Simulator(circuit)

    generator = TruthTableGenerator(
        simulator,
        [a, b],
        out
    )

    original_table = generator.generate()

    data = CircuitSerializer.serialize(
        circuit
    )

    restored_circuit = (
        CircuitSerializer.deserialize(data)
    )
    
    components = {
        component.name: component
        for component in restored_circuit.get_components()
    }

    restored_a = components["A"]
    restored_b = components["B"]
    restored_out = components["OUT"]
    
    restored_simulator = Simulator(
        restored_circuit
    )

    restored_generator = (
        TruthTableGenerator(
            restored_simulator,
            [restored_a, restored_b],
            restored_out
        )
    )

    restored_table = (
        restored_generator.generate()
    )
    
    assert original_table == restored_table