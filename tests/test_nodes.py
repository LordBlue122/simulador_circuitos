import sys
from pathlib import Path

# use pytest always

# /py route.exe/ -m pytest tests/test_gates.py

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.logic.components.input_node import InputNode
from src.logic.components.output_node import OutputNode

def test_input_node():

    node = InputNode("A")

    assert node.evaluate() is False

    node.set_value(True)

    assert node.evaluate() is True
    
def test_output_node():

    node = OutputNode("OUT")

    assert node.evaluate() is False

    node.set_value(True)

    assert node.evaluate() is True