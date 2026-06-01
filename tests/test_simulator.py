import sys
from pathlib import Path

# use pytest always

# /py route.exe/ -m pytest tests/test_gates.py

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.circuits.circuit import Circuit
from src.logic.simulation.simulator import Simulator

from src.logic.components.input_node import InputNode
from src.logic.components.output_node import OutputNode

from src.logic.components.gates.and_gate import AndGate


def test_and_simulation():

    circuit = Circuit()

    a = InputNode("A", True)
    b = InputNode("B", True)

    gate = AndGate()

    out = OutputNode("OUT")

    circuit.add_component(a)
    circuit.add_component(b)
    circuit.add_component(gate)
    circuit.add_component(out)

    circuit.connect(a, gate, 0)
    circuit.connect(b, gate, 1)
    circuit.connect(gate, out, 0)

    simulator = Simulator(circuit)

    simulator.run()

    assert out.evaluate() is True