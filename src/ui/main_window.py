import tkinter as tk

from src.ui.palette_panel import (
    PalettePanel
)

from src.ui.workspace_canvas import (
    WorkspaceCanvas
)


class MainWindow(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title(
            "Simulador de Circuitos Lógicos"
        )

        self.geometry("1000x600")

        self._build_ui()

    def _build_ui(self):

        self.palette = PalettePanel(
            self,
            self.on_gate_selected
        )

        self.palette.pack(
            side="left",
            fill="y"
        )

        self.workspace = WorkspaceCanvas(
            self
        )

        self.workspace.pack(
            side="right",
            fill="both",
            expand=True
        )

    def on_gate_selected(
        self,
        gate_type
    ):
        self.workspace.add_gate(
            gate_type
        )