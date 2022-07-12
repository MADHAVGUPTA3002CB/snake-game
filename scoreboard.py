from turtle import Turtle,Screen

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        self.color("white")
        self.penup()
        self.goto(0,280)
        file=open("C:\\New folder\\python\\snakegame\\data.txt")
        self.highscore=int(file.read())
        file.close()
        self.updatescore()
    def updatescore(self):
        self.write(f"SCORE:{self.score} HIGH SCORE :{self.highscore}",move=False,align="center",font=("Arial",20,"normal"))

    def incscore(self):
        self.score+=1
        self.clear()
        self.updatescore()
    
    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            file=open("C:\\New folder\\python\\snakegame\\data.txt","w")
            file.write(f"{self.highscore}")
            file.close()
        self.score=0
        self.clear()
        self.updatescore()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER",move=False,align="center",font=("Arial",20,"normal"))


