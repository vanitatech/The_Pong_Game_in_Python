from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move = 5
        self.y_move = 5

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9  


    #ball collision with walls
    def check_collision_with_walls(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.bounce_y()

    #ball collision with paddles
    def check_collision_with_paddle(self, paddle):
        if self.distance(paddle) < 50 and (self.xcor() > 320 or self.xcor() < -320):
            self.bounce_x()

    
    def paddle_miss(self):
        if self.xcor() > 380:
            return "right"
        elif self.xcor() < -380:
            return "left"

  
    
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
    