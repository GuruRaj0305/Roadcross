from turtle import Turtle



FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.updatebord()

    def updatescore(self):
        self.level += 1
        self.updatebord()

    def updatebord(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def gameover(self):
        self.goto(-80,0)
        self.write("GameOver", align="left", font=FONT)



