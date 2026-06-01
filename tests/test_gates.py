import sys
from pathlib import Path

# use pytest always

# /py route.exe/ -m pytest tests/test_gates.py

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.components.gates.and_gate import AndGate
from src.logic.components.gates.or_gate import OrGate
from src.logic.components.gates.xor_gate import XorGate
from src.logic.components.gates.not_gate import NotGate


def test_and_gate():

    gate = AndGate("AND_1")

    gate.inputs = [False, False]
    assert gate.evaluate() is False

    gate.inputs = [False, True]
    assert gate.evaluate() is False

    gate.inputs = [True, False]
    assert gate.evaluate() is False

    gate.inputs = [True, True]
    assert gate.evaluate() is True


def test_or_gate():

    gate = OrGate("OR_1")

    gate.inputs = [False, False]
    assert gate.evaluate() is False

    gate.inputs = [False, True]
    assert gate.evaluate() is True

    gate.inputs = [True, False]
    assert gate.evaluate() is True

    gate.inputs = [True, True]
    assert gate.evaluate() is True


def test_xor_gate():

    gate = XorGate("XOR_1")

    gate.inputs = [False, False]
    assert gate.evaluate() is False

    gate.inputs = [False, True]
    assert gate.evaluate() is True

    gate.inputs = [True, False]
    assert gate.evaluate() is True

    gate.inputs = [True, True]
    assert gate.evaluate() is False


def test_not_gate():

    gate = NotGate("NOT_1")

    gate.inputs = [False]
    assert gate.evaluate() is True

    gate.inputs = [True]
    assert gate.evaluate() is False