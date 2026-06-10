import tkinter as tk
from tkinter import ttk


class TruthTableWindow(tk.Toplevel):

    def __init__(
        self,
        parent,
        input_nodes,
        output_nodes,
        table
    ):
        super().__init__(parent)

        self.title(
            "Tabla de Verdad"
        )

        self.geometry(
            "700x400"
        )

        self.input_nodes = input_nodes
        self.output_nodes = output_nodes
        self.table = table

        self.build_ui()

    def build_ui(self):

        columns = []

        for node in self.input_nodes:
            columns.append(node.name)

        for node in self.output_nodes:
            columns.append(node.name)

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings"
        )

        for column in columns:

            self.tree.heading(
                column,
                text=column
            )

            self.tree.column(
                column,
                width=100,
                anchor="center"
            )

        for row in self.table:

            values = []

            for value in row["inputs"]:
                values.append(
                    int(value)
                )

            for value in row["outputs"]:
                values.append(
                    int(value)
                )

            self.tree.insert(
                "",
                "end",
                values=values
            )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )