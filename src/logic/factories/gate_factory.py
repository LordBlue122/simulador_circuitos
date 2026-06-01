from src.logic.components.gates.and_gate import AndGate
from src.logic.components.gates.or_gate import OrGate
from src.logic.components.gates.xor_gate import XorGate
from src.logic.components.gates.not_gate import NotGate


class GateFactory:

    _gate_registry = {
        "AND": AndGate,
        "OR": OrGate,
        "XOR": XorGate,
        "NOT": NotGate
    }

    @classmethod
    def create(
        cls,
        gate_type: str,
        name: str
    ):
        gate_type = gate_type.upper()

        if gate_type not in cls._gate_registry:
            raise ValueError(
                f"Compuerta no soportada: {gate_type}"
            )

        return cls._gate_registry[gate_type](name)