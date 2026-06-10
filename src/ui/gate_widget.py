from src.ui.pin_widget import PinWidget
from src.logic.components.input_node import InputNode
from src.logic.components.output_node import OutputNode
from src.logic.components.gates.gate import Gate
from src.logic.components.gates.not_gate import NotGate

class GateWidget:

    WIDTH = 80
    HEIGHT = 40

    def __init__(
        self,
        canvas,
        component,
        x,
        y
    ):

        self.canvas = canvas

        self.component = component

        self.x = x
        self.y = y

        self.rect_id = None
        self.text_id = None
        
        self.input_pins = []
        self.output_pin = None
        
        self.create_pins()

        self.draw()
        
    #    self.canvas.tag_bind(
    #        self.rect_id,
    #        "<Button-3>",
    #        self.on_connect_click
    #    )

    #    self.canvas.tag_bind(
    #        self.text_id,
    #        "<Button-3>",
    #        self.on_connect_click
    #    )

    def draw(self):

        self.rect_id = self.canvas.create_rectangle(
            self.x,
            self.y,
            self.x + self.WIDTH,
            self.y + self.HEIGHT
        )

        self.text_id = self.canvas.create_text(
            self.x + self.WIDTH / 2,
            self.y + self.HEIGHT / 2, 
            text=self.component.name
        )

    def move(self, dx, dy):

        self.canvas.move(
            self.rect_id,
            dx,
            dy
        )

        self.canvas.move(
            self.text_id,
            dx,
            dy
        )
        
        for pin in self.input_pins:
            pin.move(dx, dy)

        if self.output_pin:
            self.output_pin.move(dx, dy)

        self.x += dx
        self.y += dy
        
    def contains(
        self,
        item_id
    ):

        if item_id in (
            self.rect_id,
            self.text_id
        ):
            return True

        for pin in self.input_pins:

            if pin.contains(item_id):
                return True

        if self.output_pin and self.output_pin.contains(item_id):
            return True

        return False
        
    def get_output_position(self):

        if self.output_pin:
            return self.output_pin.get_position()

        return None

    def get_output_position(self):

        return self.output_pin.get_position()
        
    # def on_connect_click(self, event):
    #     self.canvas.handle_connection_click(
    #         self
    # )
        
    def create_pins(self):

        self.input_pins = []
        self.output_pin = None

        if isinstance(
            self.component,
            InputNode
        ):

            self.output_pin = PinWidget(
                self.canvas,
                self,
                self.x + self.WIDTH,
                self.y + self.HEIGHT // 2,
                PinWidget.OUTPUT
            )

        elif isinstance(
            self.component,
            OutputNode
        ):

            self.input_pins.append(

                PinWidget(
                    self.canvas,
                    self,
                    self.x,
                    self.y + self.HEIGHT // 2,
                        PinWidget.INPUT,
                    0
                )
            )

        else:

            if isinstance(self.component, NotGate):

                self.input_pins.append(

                    PinWidget(
                        self.canvas,
                        self,
                        self.x,
                        self.y + self.HEIGHT // 2,
                        PinWidget.INPUT,
                        0
                    )
                )

            else:

                self.input_pins = [

                    PinWidget(
                        self.canvas,
                        self,
                        self.x,
                        self.y + 10,
                        PinWidget.INPUT,
                        0
                    ),

                    PinWidget(
                        self.canvas,
                        self,
                        self.x,
                        self.y + self.HEIGHT - 10,
                        PinWidget.INPUT,
                        1
                    )
                ]

            self.output_pin = PinWidget(
                self.canvas,
                self,
                self.x + self.WIDTH,
                self.y + self.HEIGHT // 2,
                PinWidget.OUTPUT
            )