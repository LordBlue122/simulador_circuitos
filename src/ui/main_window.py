import tkinter as tk

from src.ui.palette_panel import (
    PalettePanel
)

from src.ui.workspace_canvas import (
    WorkspaceCanvas
)

from src.ui.property_panel import (
    PropertyPanel
)

from src.logic.simulation.simulator import (
    Simulator
)

from src.logic.simulation.simulator import Simulator

from src.truth_table.generator import (
    TruthTableGenerator
)

from src.logic.components.input_node import (
    InputNode
)

from src.logic.components.output_node import (
    OutputNode
)

from src.ui.truth_table_window import (
    TruthTableWindow
)


class MainWindow(tk.Tk):

    def __init__(self):

        super().__init__()

        self.title(
            "Simulador de Circuitos Lógicos"
        )
        
        self.properties = PropertyPanel(
            self
        )
        
        self.properties.pack(
            side="right",
            fill="y"
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
            self,
            self.on_component_selected
        )
        
        self.simulate_button = tk.Button(
            self,
            text="Simular",
            command=self.simulate
        )
        
        self.truth_table_button = tk.Button(
            self,
            text="Tabla de Verdad",
            command=self.generate_truth_table
        )

        self.truth_table_button.pack(
            side="bottom",
            fill="x"
        )
        
        self.simulate_button.pack(
            side="bottom",
            fill="x"
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
        
    def on_component_selected(
        self,
        component
    ):

        self.properties.show_component(
            component
        )
        
    def simulate(self):

        simulator = Simulator(
            self.workspace.circuit
        )

        simulator.run()
        
        if (
            self.workspace.selected_widget
        ):

            self.properties.show_component(
                self.workspace.selected_widget.component
            )

        print("\n=== RESULTADOS ===")

        for component in (
            self.workspace.circuit.get_components()
        ):

            if hasattr(
                component,
                "value"
            ):

                print(
                    component.name,
                    "=",
                    component.value
                )
                
    def generate_truth_table(self):

        inputs = []
        outputs = []

        for component in (
            self.workspace.circuit.get_components()
        ):

            if isinstance(
                component,
                InputNode
            ):
                inputs.append(component)

            elif isinstance(
                component,
                OutputNode
            ):
                outputs.append(component)

        if not inputs:

            print("No hay inputs")
            return

        if not outputs:

            print("No hay outputs")
            return

        simulator = Simulator(
            self.workspace.circuit
        )

        generator = TruthTableGenerator(
            simulator,
            inputs,
            outputs
        )

        table = generator.generate()

        TruthTableWindow(
            self,
            inputs,
            outputs,
            table
        )