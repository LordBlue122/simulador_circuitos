import sys
from pathlib import Path
import pytest



sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.factories.gate_factory import GateFactory

from src.logic.components.gates.and_gate import AndGate
from src.logic.components.gates.or_gate import OrGate
from src.logic.components.gates.xor_gate import XorGate
from src.logic.components.gates.not_gate import NotGate

def test_create_and_gate():

    gate = GateFactory.create("AND")

    assert isinstance(gate, AndGate)


def test_create_or_gate():

    gate = GateFactory.create("OR")

    assert isinstance(gate, OrGate)


def test_create_xor_gate():

    gate = GateFactory.create("XOR")

    assert isinstance(gate, XorGate)


def test_create_not_gate():

    gate = GateFactory.create("NOT")

    assert isinstance(gate, NotGate)

def test_invalid_gate():

    with pytest.raises(ValueError):
        GateFactory.create("NAND")