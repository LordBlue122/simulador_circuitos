class PinWidget:

    RADIUS = 4

    INPUT = "input"
    OUTPUT = "output"

    def __init__(
        self,
        canvas,
        owner,
        x,
        y,
        pin_type,
        index=None
    ):

        self.canvas = canvas
        
        self.owner = owner
        
        self.connected_wire = None
        self.hitbox_id = None

        self.x = x
        self.y = y

        self.pin_type = pin_type
        self.index = index

        self.circle_id = None

        self.draw()
        
        self.canvas.tag_bind(
            self.circle_id,
            "<Button-3>",
            self.on_connect_click
        )

        self.canvas.tag_bind(
            self.circle_id,
            "<Enter>",
            self.on_mouse_enter
        )

        self.canvas.tag_bind(
            self.circle_id,
            "<Leave>",
            self.on_mouse_leave
        )

    def draw(self):
        
        r = self.RADIUS
        
        hitbox_radius = 14

        self.hitbox_id = self.canvas.create_oval(
            self.x - hitbox_radius,
            self.y - hitbox_radius,
            self.x + hitbox_radius,
            self.y + hitbox_radius,
            outline="",
            fill=""
        )
        
        self.circle_id = self.canvas.create_oval(
            self.x - r,
            self.y - r,
            self.x + r,
            self.y + r
        )
        
        self.canvas.tag_bind(
            self.circle_id,
            "<Button-3>",
            self.on_connect_click
        )
        
    def is_connected(self):
        return self.connected_wire is not None
        
    def on_connect_click(self, event):

        print("PIN CLICK")
        
        self.canvas.handle_pin_click(
            self
        )

    def move(self, dx, dy):

        self.canvas.move(
            self.circle_id,
            dx,
            dy
        )
        
        self.canvas.move(
            self.hitbox_id,
            dx,
            dy
        )

        self.x += dx
        self.y += dy

    def contains(self, item_id):

        return item_id in (
            self.circle_id,
            self.hitbox_id
        )

    def get_position(self):

        return self.x, self.y
    
    def is_input(self):

        return self.pin_type == self.INPUT


    def is_output(self):

        return self.pin_type == self.OUTPUT
    
    def on_mouse_enter(self, event):

        self.canvas.config(
            cursor="crosshair"
        )


    def on_mouse_leave(self, event):

        self.canvas.config(
            cursor=""
        )