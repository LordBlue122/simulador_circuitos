class WireWidget:

    def __init__(
        self,
        canvas,
        wire,
        source_pin,
        target_pin
    ):

        self.canvas = canvas

        self.wire = wire

        self.source_pin = source_pin
        self.target_pin = target_pin

        self.line_id = None

        self.draw()

    def draw(self):

        x1, y1 = self.source_pin.get_position()
        x2, y2 = self.target_pin.get_position()

        self.line_id = self.canvas.create_line(
            x1,
            y1,
            x2,
            y2,
            width=2
        )

    def update_position(self):

        x1, y1 = self.source_pin.get_position()
        x2, y2 = self.target_pin.get_position()

        self.canvas.coords(
            self.line_id,
            x1,
            y1,
            x2,
            y2
        )