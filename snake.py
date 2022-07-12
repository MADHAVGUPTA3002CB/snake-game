from turtle import Turtle,Screen
class Snake:
    def __init__(self):
        # a=["snksr","snkpt","snkpr"]
        snksr=Turtle()
        snkpt=Turtle()
        snkpr=Turtle()
        self.a=[snksr,snkpt,snkpr]
        self.b=[]
        self.head=self.a[0]
        self.create_samp()
    def create_samp(self):
        pos=0
        for i in self.a:
            i.shape("square")
            i.color("white")
            i.penup()
            i.setpos(pos,0)
            pos-=20
            self.b.append(i)
    def addsegment(self):
        i=Turtle()
        i.shape("square")
        i.color("white")
        i.penup()
        i.setpos(self.b[-1].pos())
        self.b.append(i)

    def reset(self):
        for segment in self.b:
            segment.color("black")
        self.b.clear()
        self.create_samp()
        self.head=self.a[0]
    def move(self):
        s=self.b
        for i in range(len(s)-1,0,-1):
            x=s[i-1].xcor()
            y=s[i-1].ycor()
            s[i].goto(x,y)
        s[0].fd(20) 
    def up(self):
        s=self.b
        if s[0].heading()==0:
            s[0].right(-90)
        if s[0].heading()==180:
                s[0].right(90)
    def down(self):
        s=self.b
        if s[0].heading()==0:
            s[0].right(90)
        if s[0].heading()==180:
                s[0].right(-90)
    def right(self):
        s=self.b
        if s[0].heading()==270:
            s[0].right(-90)
        if s[0].heading()==90:
            s[0].right(90)
    def left(self):
        s=self.b
        if s[0].heading()==270:
            s[0].right(90)
        if s[0].heading()==90:
            s[0].right(-90)