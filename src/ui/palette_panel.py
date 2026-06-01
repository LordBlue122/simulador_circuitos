import tkinter as tk

from src.logic.factories.gate_factory import GateFactory


class PalettePanel(tk.Frame):

    def __init__(
        self,
        parent,
        on_gate_selected
    ):
        super().__init__(
            parent,
            width=150
        )

        self.on_gate_selected = (
            on_gate_selected
        )

        self._build_ui()

    def _build_ui(self):

        title = tk.Label(
            self,
            text="Compuertas"
        )

        title.pack(
            pady=10
        )

        for gate_name in (
            GateFactory.get_available_gates()
        ):

            button = tk.Button(
                self,
                text=gate_name,
                command=lambda g=gate_name:
                    self.on_gate_selected(g)
            )

            button.pack(
                fill="x",
                padx=10,
                pady=2
            )