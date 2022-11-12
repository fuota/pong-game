from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.score = 0
        self.write(f"{self.score}",font=('Courier', 80, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", font=('Courier', 80, 'bold'))



