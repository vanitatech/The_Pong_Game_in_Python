from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)



    def listen_to_keys(self, up_key, down_key):
        screen = self.getscreen()
        screen.listen()
        screen.onkey(self.move_up, up_key)
        screen.onkey(self.move_down, down_key)
     

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 250:  # Prevent paddle from going off the top of the screen
            self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -250:  # Prevent paddle from going off the bottom of the screen
            self.goto(self.xcor(), new_y)

