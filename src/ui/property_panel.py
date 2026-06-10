import tkinter as tk
from src.logic.components.input_node import InputNode


class PropertyPanel(tk.Frame):

    def __init__(
        self,
        parent
    ):

        super().__init__(
            parent,
            width=200
        )

        self.name_title = tk.Label(
            self,
            text="Nombre:"
        )

        self.name_title.pack()

        self.name_value = tk.Label(
            self,
            text=""
        )

        self.name_value.pack()

        self.input_value_var = tk.BooleanVar()
        
        self.value_check = tk.Checkbutton(
            self,
            text="Valor",
            variable=self.input_value_var,
            command=self.on_input_value_changed
        )
        
        self.current_component = None

        self.type_title = tk.Label(
            self,
            text="Tipo:"
        )

        self.type_title.pack()

        self.type_value = tk.Label(
            self,
            text=""
        )

        self.type_value.pack()

    def show_component(
        self,
        component
    ):

        self.name_label.config(
            text=component.name
        )
    
    def show_component(
        self,
        component
    ):

        self.current_component = component

        self.name_value.config(
            text=component.name
        )

        self.type_value.config(
            text=type(component).__name__
        )

        self.value_check.pack_forget()

        if isinstance(
            component,
            InputNode
        ):

            self.input_value_var.set(
                component.value
            )

            self.value_check.pack(
                pady=10
            )
            
    def on_input_value_changed(self):

        if self.current_component is None:
            return

        if not isinstance(
            self.current_component,
            InputNode
        ):
            return

        self.current_component.set_value(
            self.input_value_var.get()
        )

        print(
            self.current_component.name,
            "=",
            self.current_component.value
        )