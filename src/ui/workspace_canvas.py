import tkinter as tk
from src.logic.circuits.circuit import Circuit
from src.ui.widgets.wire_widget import WireWidget


class WorkspaceCanvas(tk.Canvas):

    def __init__(self, parent):

        super().__init__(
            parent,
            bg="white"
        )

        self.gate_count = 0
        self.gate_widgets = []
        self.wire_widgets = []
        self.selected_widget = None
        self.connection_source = None
        self.component_widgets = {}

        self.last_x = 0
        self.last_y = 0

        self.circuit = Circuit()
        self.component_counter = 0

        self.bind("<Button-1>", self.on_mouse_press)
        self.bind("<B1-Motion>", self.on_mouse_drag)
        self.bind("<ButtonRelease-1>", self.on_mouse_release)

    def add_gate(self, gate_type):

        self.gate_count += 1

        x = 200
        y = 100 + (self.gate_count * 60)

        from src.logic.factories.gate_factory import GateFactory
        from src.ui.gate_widget import GateWidget

        self.component_counter += 1

        name = f"{gate_type}_{self.component_counter}"

        component = GateFactory.create(
            gate_type,
            name
        )

        self.circuit.add_component(component)

        widget = GateWidget(
            self,
            component,
            x,
            y
        )

        self.gate_widgets.append(widget)
        self.component_widgets[component.name] = widget

        print(len(self.circuit.get_components()))

    def find_widget(self, item_id):

        for widget in self.gate_widgets:

            if widget.contains(item_id):
                return widget

        return None


    def on_mouse_press(self, event):

        item = self.find_overlapping(
            event.x,
            event.y,
            event.x,
            event.y
        )
        
        if not item:
            return

        item_id = item[-1]
        
        pin = self.find_pin(item_id)

        if pin:
            return

        widget = self.find_widget(item_id)

        if widget:

            self.selected_widget = widget

            self.last_x = event.x
            self.last_y = event.y

    def on_mouse_drag(self, event):

        if not self.selected_widget:
            return

        dx = event.x - self.last_x
        dy = event.y - self.last_y

        self.selected_widget.move(dx, dy)
        
        self.update_wires()

        self.last_x = event.x
        self.last_y = event.y

    def on_mouse_release(self, event):

        self.selected_widget = None
        
    def start_connection(self, gate_widget):

        self.connection_source = gate_widget

        print(
            f"Origen seleccionado: "
            f"{gate_widget.component.name}"
        )
        
    def finish_connection(self, target_pin):

        if self.connection_source is None:
            return

        source_pin = self.connection_source

        if source_pin.owner == target_pin.owner:

            self.connection_source = None   
            return

        if self.circuit.is_input_connected(
            target_pin.owner.component,
            target_pin.index
        ):

            print(
                f"Input {target_pin.index} ocupado"
            )

            self.connection_source = None
            return
        
        if target_pin.is_connected():

            print(
                f"Input {target_pin.index} ocupado"
            )

            self.connection_source = None
            return
        
        wire = self.circuit.connect(
            source_pin.owner.component,
            target_pin.owner.component,
            target_pin.index
        )

        wire_widget = WireWidget(
            self,
            wire,
            source_pin,
            target_pin
        )

        self.wire_widgets.append(
            wire_widget
        )

        self.connection_source = None

        print(
            f"{source_pin.owner.component.name}"
            f" -> "
            f"{target_pin.owner.component.name}"
            f" [input {target_pin.index}]"
        )

    def handle_connection_click(
        self,
    gate_widget
    ):
        if self.connection_source is None:
            self.start_connection(gate_widget)
        else:
            self.finish_connection(gate_widget)

    def update_wires(self):
        for wire_widget in self.wire_widgets:
            wire_widget.update_position()
            
    def find_pin(self, item_id):
        for gate in self.gate_widgets:
            for pin in gate.input_pins:
                if pin.contains(item_id):
                    return pin
            if gate.output_pin and gate.output_pin.contains(item_id):
                return gate.output_pin
        return None
    
    def handle_pin_click(self, pin):

        if self.connection_source is None:

            if pin.is_output():

                self.connection_source = pin

                print(
                    f"Salida seleccionada "
                    f"{pin.owner.component.name}"
                )

            return

        if not pin.is_input():
            return

        self.finish_connection(pin)