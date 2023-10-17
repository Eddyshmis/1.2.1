# a121_catch_a_turtle.py
#-----import statements-----
import turtle as tl
from random import randint
import leaderboard as lb
#-----game configuration----
color_turtle = "green"
color_pen = "black"
turtle_shape = "turtle"
pen_size = 10
turtle_size = 10
counter_interval = 1000
points = 0
timer = 2


turtle_sizes = [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0]
screen = tl.Screen()
screen.bgcolor("lightgreen")
#-----initialize turtle-----
turtle_1 = tl.Turtle()
turtle_1.shape(turtle_shape)
turtle_1.speed(0)
turtle_1.pensize(pen_size)
turtle_1.shapesize(turtle_size)
turtle_1.color(color_turtle)
turtle_1.pencolor(color_pen)
turtle_1.setheading(90)
turtle_1.up()
display_turtle = tl.Turtle()
display_turtle.hideturtle()
display_turtle.up()






display_turtle.goto(0,160)
display_turtle.write("start",False,align="center",font=("Arial",20,"normal"))

#-----game functions--------
def timer_event():
    global timer,time_up,points
    display_turtle.clear()
    
    display_turtle.write(f"timer:{timer}\npoints:{points}",False,"center",("Arial",20,"normal"))
    
    if timer <= 0:
        display_turtle.clear()
        display_turtle.write(f"FINISHED {points}",False,"center",("Arial",20,"normal"))
        display_end()
        turtle_1.onclick(None)

    else:
        turtle_1.onclick(clicked_event)
        
        screen.ontimer(timer_event,counter_interval)
        timer -= 1


def change_pos():
    x = randint(-400,300)
    y = randint(-400,300)
    turtle_1.goto(x,y)
    turtle_1.shapesize(turtle_sizes[randint(0,18)])

def clicked_event(X,Y):
    global points
    points += 1
    turtle_1.color("red")
    turtle_1.stamp()
    turtle_1.color("green")
    
    change_pos()

def start_game(x,y):
    turtle_1.onclick(None)
    display_turtle.goto(-400,340)
    timer_event()

def display_end():
    display_turtle.goto(0,300)
    display_turtle.color("lightslategray")
    x,y = display_turtle.pos()
    y -= 100

    new_player_name = tl.textinput("ask name","type your name")
    if new_player_name == None:
        new_player_name = ""
    if len(new_player_name) > 0:
        lb.set_new_player(new_player_name,points)


    turtle_1.goto(1000,1000)
    lb.check_file()
    all_info = lb.get_player_data()
    
    display_turtle.write("player | points",False,"center",("Arial",20,"normal"))
    for player in all_info:
        display_turtle.goto(x,y)
        display_turtle.write(f"""{player}  -->  {all_info[player]}""",False,"center",("Arial",20,"normal"))
        y -= 50
#-----events----------------



turtle_1.onclick(start_game)



screen.mainloop()