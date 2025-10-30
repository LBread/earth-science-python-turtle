import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#0B0E2A")
screen.setup(width=800, height=800)
t.speed(0)
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
def layer(radius, color_, y_level,rotation):
    t.sety(y_level)
    t.begin_fill()
    t.color(color_)
    t.circle(radius,rotation)
    t.goto(0,-40)
    t.end_fill()
layer(150,"OliveDrab",-190,360)
layer(140,"#873A1B",-180,360)
layer(120,"#9E3018",-160,360)
layer(70,"#CC7A1D",-110,360)
layer(35,"#D99C18",-75,360)
layer(150,"OliveDrab",-190,270)

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
def definitions_of_things(sent1,sent2,x,y,Defcolor):
    t.goto(x,y)
    t.color(Defcolor)
    t.write(sent1, font=("Arial", 8, "bold"), align="left")
    t.sety(y-15)
    t.write(sent2, font=("Arial", 8, "bold"), align="left")
definitions_of_things("The lithosphere is the rigid cold outer layer that includes the crust and the uppermost part of the mantle"," It’s broken into tectonic plates that move slowly over the softer layer beneath.",-500,110,"OliveDrab")
definitions_of_things("The asthenosphere lies just below the lithosphere and is made of partially hot molten rock that can flow.", "This layer allows the tectonic plates above it to move and shift.",-725,-90,"#873A1B")
definitions_of_things("The mesosphere is the strong, lower part of the mantle beneath the asthenosphere.","It’s made of solid rock that moves more slowly due to higher pressure and density.", -450,-240,"#9E3018")
definitions_of_things("The outer core is a layer of  extremely hot molten iron and nickel that surrounds the inner core.", "Its flowing metal creates Earth’s magnetic field.", 75,-240,"#CC7A1D")
definitions_of_things("The inner core is the solid center of the Earth made mostly of hot iron and nickel.","It remains solid because of the immense pressure at Earth’s center despite extremely high temperatures.", 175,-90,"#D99C18")
definitions_of_things("The Atmosphere is the layer of gases surrounding Earth ""that provides the air we breathe ","and protects us from the Sun’s harmful radiation."" It also helps regulate the planet’s temperature and weather patterns.",275,215,"#23838A")
definitions_of_things("The Geosphere is the solid part of the Earth, including rocks, soil, and the layers beneath the surface.", "It provides the foundation for landforms like mountains, valleys, and volcanoes.",275,170,"#42A115")
definitions_of_things("The hydrosphere includes all the water on Earth, such as oceans, rivers, lakes, glaciers, and even water vapor in the air. ","It is essential for all living things and constantly moves through the water cycle.",275,125,"#192BD1")
definitions_of_things("The biosphere consists of all living organisms on Earth, from tiny microbes to large animals and plants.", "It interacts with the other spheres to support and sustain life.",275,80,"#19D18B")
definitions_of_things("Convection currents are the movement of fluids (like air or magma) caused by differences in temperature and density.", "Warmer, less dense material rises while cooler, denser material sinks, creating a continuous circular flow.",275,260,"#76B3F8")
screen.update()
screen.exitonclick()