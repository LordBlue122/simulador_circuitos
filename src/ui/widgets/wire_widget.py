class WireWidget:

    def __init__(
        self,
        canvas,
        wire,
        source_widget,
        target_widget
    ):

        self.canvas = canvas

        self.wire = wire

        self.source_widget = source_widget
        self.target_widget = target_widget

        self.line_id = None

        self.draw()

    def draw(self):

        x1, y1 = self.source_widget.get_output_position()
        x2, y2 = self.target_widget.get_input_position()

        self.line_id = self.canvas.create_line(
            x1,
            y1,
            x2,
            y2,
            width=2
        )

    def update_position(self):

        x1, y1 = self.source_widget.get_output_position()
        x2, y2 = self.target_widget.get_input_position()

        self.canvas.coords(
            self.line_id,
            x1,
            y1,
            x2,
            y2
        )