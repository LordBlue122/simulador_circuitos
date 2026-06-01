import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.circuits.circuit import Circuit
from src.logic.components.gates.and_gate import AndGate
from src.logic.components.gates.or_gate import OrGate


def test_circuit_creation():

    circuit = Circuit()

    and_gate = AndGate()
    or_gate = OrGate()

    circuit.add_component(and_gate)
    circuit.add_component(or_gate)

    assert len(circuit.get_components()) == 2
    
    
def test_circuit_connection():

    circuit = Circuit()

    and_gate = AndGate()
    or_gate = OrGate()

    circuit.add_component(and_gate)
    circuit.add_component(or_gate)

    wire = circuit.connect(
        source=and_gate,
        target=or_gate,
        target_input_index=0
    )

    assert len(circuit.get_wires()) == 1

    assert wire.source == and_gate
    assert wire.target == or_gate

    assert wire.target_input_index == 0
    
    
def test_multiple_connections():

    circuit = Circuit()

    gate_a = AndGate()
    gate_b = OrGate()

    circuit.add_component(gate_a)
    circuit.add_component(gate_b)

    circuit.connect(
        source=gate_a,
        target=gate_b,
        target_input_index=0
    )

    circuit.connect(
        source=gate_a,
        target=gate_b,
        target_input_index=1
    )

    assert len(circuit.get_wires()) == 2
    
    
def test_remove_component():

    circuit = Circuit()

    gate = AndGate()

    circuit.add_component(gate)

    assert len(circuit.get_components()) == 1

    circuit.remove_component(gate)

    assert len(circuit.get_components()) == 0