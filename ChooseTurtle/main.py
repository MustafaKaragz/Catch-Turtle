import turtle
import random

#screen
screen=turtle.Screen()
screen.bgcolor("LightGreen")
screen.title("Choose Turtle")
FONT=("Verdana",28,"normal")
x_coord=[-30,-20,-10,0,10,20,30]
y_coord=[20,10,0,-10]
turtle_list=[]
score=0
game_over=False



                                # MUSTAFA KARAGÖZ

#scoreboard
score_turtle = turtle.Turtle()

#finish
finish_turtle=turtle.Turtle()

def scoreturtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    topheight=screen.window_height()
    score_turtle.penup()
    score_turtle.setpos(0,topheight*0.5+20)
    score_turtle.pendown()
    score_turtle.write(arg="Score:0",move=False,align="center",font=FONT)


def make_turtle(x,y):
    t1=turtle.Turtle()

    def click(x,y):
        global score
        score+=1
        score_turtle.clear()
        score_turtle.write(arg=f"Score:{score}",move=False,align="center",font=FONT)

    t1.penup()
    t1.onclick(click)
    t1.shape("turtle")
    t1.shapesize(2,2)
    t1.color("Darkgreen")
    t1.goto(x*10,y*10)
    turtle_list.append(t1)

def turtlecoord():
    for x in x_coord:
        for y in y_coord:
            make_turtle(x,y)


def hide_turtle():
    for t in turtle_list:
        t.hideturtle()


def show_turtle():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        screen.ontimer(show_turtle,500)

def finish(time):
    global game_over
    finish_turtle.hideturtle()
    finish_turtle.penup()
    finish_turtle.color("Red")
    topheight=screen.window_height()
    finish_turtle.setpos(0,topheight*0.5-140)
    finish_turtle.pendown()
    finish_turtle.clear()
    if time>0:
        finish_turtle.clear()
        finish_turtle.write(arg=f"Time:{time}",move=False,align="center",font=FONT)
        screen.ontimer(lambda:finish(time-1),1000)
    else:
        game_over=True
        finish_turtle.clear()
        hide_turtle()
        finish_turtle.write(arg="Game Over",move=False,align="center",font=FONT)


turtle.tracer(0)
scoreturtle()
turtlecoord()
hide_turtle()
show_turtle()
finish(10)
turtle.tracer(1)

turtle.mainloop()