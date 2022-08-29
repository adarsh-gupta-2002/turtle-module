import turtle
import time
import random

t = turtle.Turtle()
s = turtle.Screen()
t.shape("turtle")
s.title("Night Sky")
s.screensize(800 , 500 , bg="black")
t.pencolor("white")


t.speed(0)
def star():
    
    for i in range(5):
        t.pendown()
        t.forward(10)
        # time.sleep(2)
        t.right(144)
t.hideturtle()   
s.colormode(255)
while True:
    
    x = random.randint(-400 , 250)
    y = random.randint(-400,250)
    r = random.randint(0 , 255)
    g = random.randint(0,255)
    b = random.randint(0 , 255)
    t.pencolor(r,g,b)
    t.penup()
    t.goto(x,y)
    star()
turtle.done()