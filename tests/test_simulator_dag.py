import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.circuits.circuit import Circuit
from src.logic.simulation.simulator import Simulator

from src.logic.components.input_node import InputNode
from src.logic.components.output_node import OutputNode

from src.logic.components.gates.and_gate import AndGate
from src.logic.components.gates.or_gate import OrGate


def test_multilevel_circuit_true():

    circuit = Circuit()

    a = InputNode("A", True)
    b = InputNode("B", True)
    c = InputNode("C", False)

    and_gate = AndGate("AND_1")
    or_gate = OrGate("OR_1")

    out = OutputNode("OUT")

    circuit.add_component(a)
    circuit.add_component(b)
    circuit.add_component(c)

    circuit.add_component(and_gate)
    circuit.add_component(or_gate)

    circuit.add_component(out)

    circuit.connect(a, and_gate, 0)
    circuit.connect(b, and_gate, 1)

    circuit.connect(and_gate, or_gate, 0)
    circuit.connect(c, or_gate, 1)

    circuit.connect(or_gate, out, 0)

    simulator = Simulator(circuit)

    simulator.run()

    assert out.evaluate() is True


def test_multilevel_circuit_false():

    circuit = Circuit()

    a = InputNode("A", False)
    b = InputNode("B", True)
    c = InputNode("C", False)

    and_gate = AndGate("AND_1")
    or_gate = OrGate("OR_1")

    out = OutputNode("OUT")

    circuit.add_component(a)
    circuit.add_component(b)
    circuit.add_component(c)

    circuit.add_component(and_gate)
    circuit.add_component(or_gate)

    circuit.add_component(out)

    circuit.connect(a, and_gate, 0)
    circuit.connect(b, and_gate, 1)

    circuit.connect(and_gate, or_gate, 0)
    circuit.connect(c, or_gate, 1)

    circuit.connect(or_gate, out, 0)

    simulator = Simulator(circuit)

    simulator.run()

    assert out.evaluate() is False