# a121_catch_a_turtle.py
#-----import statements-----
import turtle as tl
from random import randint
#-----game configuration----
timer = 10
time_up = False
color_turtle = "green"
color_pen = "black"
pen_size = 10
turtle_size = 10
counter_interval = 1000
points = 0
screen = tl.Screen()


#-----initialize turtle-----
turtle_1 = tl.Turtle()
turtle_1.speed(0)
turtle_1.pensize(pen_size)
turtle_1.shapesize(turtle_size)
turtle_1.color(color_turtle)
turtle_1.pencolor(color_pen)

display_turtle = tl.Turtle()
display_turtle.hideturtle()
display_turtle.up()
display_turtle.goto(-400,350)


#-----game functions--------
def timer_event():
    global timer,time_up,points
    display_turtle.clear()
    
    display_turtle.write(f"timer:{timer}\npoints:{points}",False,"center",("Arial",20,"normal"))
    
    if timer <= 0:
        display_turtle.clear()
        display_turtle.write(f"FINISHED {points}",False,"center",("Arial",20,"normal"))
        time_up = True
        turtle_1.onclick(None)

    else:
        turtle_1.onclick(clicked_event)
        
        screen.ontimer(timer_event,counter_interval)
        timer -= 1


def change_pos():
    x = randint(-400,300)
    y = randint(-400,300)
    turtle_1.goto(x,y)

def clicked_event(X,Y):
    global points
    points += 1
    change_pos()
    

#-----events----------------




timer_event()


screen.mainloop()