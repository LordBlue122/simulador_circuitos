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

        self.draw()

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

        self.x += dx
        self.y += dy
        
    def contains(
        self,
        item_id
    ):

        return item_id in (
            self.rect_id,
            self.text_id
        )