from turtle import Turtle

class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.width(5)
        self.setheading(270)
        self.speed(0)
        self.color("white")

    def middle(self):
        self.hideturtle()
        self.penup()
        self.goto(0, 450)
        for _ in range(50):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)