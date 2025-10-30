import turtle
import random
import math
import time
from turtle import Shape

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#0B0E2A")
screen.setup(width=800, height=800)
t.speed(0)
t.penup()
t.hideturtle()
screen.tracer(0)

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.attributes("-fullscreen", True)

def draw_star( x, y, size, color):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

num_stars = 1000
for _ in range(num_stars):
    x = random.randint(-1000, 1000)
    y = random.randint(-800, 800)
    size = random.randint(0, 4)
    color = random.choice(["lightgray","#4c4463","#8a8bbd","#521E1E","#3c5152"]) 
    
    draw_star(x, y, size, color)
t.penup()
t.goto(0,-200)

#the main earth code
def layer(radius, color_,x,y_level,rotation):
    t.goto(x,y_level)
    t.begin_fill()
    t.color(color_)
    t.circle(radius,rotation)
    t.end_fill()
layer(160,"#6B8E23",10,-210,360)
layer(150,"#5E7E1F",0,-190,360)
layer(140,"#873A1B",0,-180,360)
layer(120,"#9E3018",0,-160,360)
layer(70,"#CC7A1D",0,-110,360)
layer(35,"#D99C18",0,-75,360)
layer(150,"#6B8E23",0,-190,180)

def draw_half_oval(start, mid, end, fill_color):
    t.color(fill_color)
    t.penup()
    t.goto(start)
    t.pendown()
    t.begin_fill()
    steps = 40
    for i in range(steps + 1):
        t_val = i / steps
        x = (1 - t_val)**2 * start[0] + 2 * (1 - t_val) * t_val * mid[0] + t_val**2 * end[0]
        y = (1 - t_val)**2 * start[1] + 2 * (1 - t_val) * t_val * mid[1] + t_val**2 * end[1]
        t.goto(x, y)
    t.goto(start)
    t.end_fill()

draw_half_oval((0, -190), (100, -40), (0, 108), "#4A6318")
draw_half_oval((0, -180), (90, -40), (0, 98), "#6B2E16")
draw_half_oval((0, -160), (80, -40), (0, 78), "#6D2211")
draw_half_oval((0, -110), (50, -40), (0, 28), "#854F13")
draw_half_oval((0, -75), (15, -40), (0, -8), "#966C13")

#basic definitons
def create_key_of_things(colortext,x,y,text):
    t.penup()
    t.color(colortext) 
    t.goto(x,y) 
    t.write(text, font=("Arial", 10, "bold"), align="left")
    t.goto(x-5.5,y+5)
    t.begin_fill()
    t.circle(2.5,360,4)
    t.end_fill()
create_key_of_things("OliveDrab",-500,125, "Lithosphere = outer layer made of rock and dirt")
create_key_of_things("#873A1B",-700,-75,"Ashthenosphere = inner layer made of minerals") 
create_key_of_things("#9E3018",-450,-225,"Mesosphere = center layer made of ores and lava") 
create_key_of_things("#CC7A1D",75,-225,"Outercore = lower layer made of molten metal and lava") 
create_key_of_things("#D99C18",175,-75,"Innercore = lowest layer made of hot iron")
create_key_of_things("#149099",300,230,"Atmosphere:")
create_key_of_things("#42A115",300,185,"Geopshere:")
create_key_of_things("#192BD1",300,140,"Hydrosphere:")
create_key_of_things("#19D18B",300,95,"Biosphere:")
create_key_of_things("#76B3F8",300,275  ,"Convection currents")
#used to make definitions of layers
def definitions_of_things(x,y,sent1,sent2,Defcolor):
    t.goto(x,y)
    t.color(Defcolor)
    t.write(sent1, font=("Arial", 8, "bold"), align="left")
    t.sety(y-15)
    t.write(sent2, font=("Arial", 8, "bold"), align="left")
definitions_of_things(-500,110,"The lithosphere is the rigid cold outer layer that includes the crust and the uppermost part of the mantle"," It’s broken into tectonic plates that move slowly over the softer layer beneath.","OliveDrab")
definitions_of_things(-725,-90,"The asthenosphere lies just below the lithosphere and is made of partially hot molten rock that can flow.", "This layer allows the tectonic plates above it to move and shift.","#873A1B")
definitions_of_things(-450,-240,"The mesosphere is the strong, lower part of the mantle beneath the asthenosphere.","It’s made of solid rock that moves more slowly due to higher pressure and density.","#9E3018")
definitions_of_things(75,-240,"The outer core is a layer of  extremely hot molten iron and nickel that surrounds the inner core.", "Its flowing metal creates Earth’s magnetic field.","#CC7A1D")
definitions_of_things(175,-90,"The inner core is the solid center of the Earth made mostly of hot iron and nickel.","It remains solid because of the immense pressure at Earth’s center despite extremely high temperatures.","#D99C18")
definitions_of_things(275,215,"The Atmosphere is the layer of gases surrounding Earth ""that provides the air we breathe ","and protects us from the Sun’s harmful radiation."" It also helps regulate the planet’s temperature and weather patterns.","#23838A")
definitions_of_things(275,170,"The Geosphere is the solid part of the Earth, including rocks, soil, and the layers beneath the surface.", "It provides the foundation for landforms like mountains, valleys, and volcanoes.","#42A115")
definitions_of_things(275,125,"The hydrosphere includes all the water on Earth, such as oceans, rivers, lakes, glaciers, and even water vapor in the air. ","It is essential for all living things and constantly moves through the water cycle.","#192BD1")
definitions_of_things(275,80,"The biosphere consists of all living organisms on Earth, from tiny microbes to large animals and plants.", "It interacts with the other spheres to support and sustain life.","#19D18B")
definitions_of_things(275,260,"Convection currents are the movement of fluids (like air or magma) caused by differences in temperature and density.", "Warmer, less dense material rises while cooler, denser material sinks, creating a continuous circular flow.","#76B3F8")
#Future code
"""
def make_definition_lines(def_x,def_y,layer_x,layer_y,line_color):
    t.color(line_color)
    t.goto(def_x,def_y)
    t.pendown()
    t.goto(layer_x,layer_y)

make_definition_lines(-500,110,)
make_definition_lines(-725,-90,)
make_definition_lines(-450,-240,)
make_definition_lines(75,-240,)
make_definition_lines(175,-90,)
make_definition_lines(275,215,)
make_definition_lines(275,170,)
make_definition_lines(275,125,)
make_definition_lines(275,80,)
make_definition_lines(275,260,)
"""
screen.update()

def create_moon_shape(screen, size=35):
    """Register a circular moon shape."""
    moon_shape = Shape("compound")
    temp_t = turtle.Turtle(visible=False)
    temp_t.penup()
    temp_t.goto(0, -size)
    temp_t.begin_poly()
    temp_t.circle(size)
    temp_t.end_poly()
    poly = temp_t.get_poly()
    moon_shape.addcomponent(poly, "lightgray", "lightgray")
    screen.register_shape("moon", moon_shape)

create_moon_shape(screen)

moon = turtle.Turtle()
moon.shape("moon")
moon.penup()
moon.speed(0)
moon.hideturtle()

radius = 400
speed = 0.05
angle = 0
moon_size = 35
running = True

def stop_animation(x=None, y=None):
    global running
    running = False

def stop_animation(x=None, y=None):
    global running
    running = False
    screen.bye()

screen.onclick(stop_animation)

while running:
    x = radius * math.cos(angle)
    y = radius * math.sin(angle) * 0.4
    scale = 0.6 + 0.4 * math.sin(angle)

    depth = (math.sin(angle) + 1) / 2 
    if depth < 0.03:
        moon.hideturtle()
    else:
        moon.showturtle()

    moon.shapesize(stretch_wid=scale, stretch_len=scale)
    moon.goto(x, y)
    screen.update()

    angle += speed
    time.sleep(0.02)
