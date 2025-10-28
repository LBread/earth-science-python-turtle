import turtle
import random
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("#0B0E2A")
screen.setup(width=800, height=800)
t.speed(0)
t.hideturtle()

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

num_stars = 100
for _ in range(num_stars):
    x = random.randint(-800, 800)
    y = random.randint(-800, 800)
    size = random.randint(2, 6)
    color = random.choice(["white", "lightgray"]) 
    
    draw_star(x, y, size, color)
t.penup()
t.goto(0,-200)
#the main earth code
def layer(radius, color_, y_level):
    t.sety(y_level)
    t.begin_fill()
    t.color(color_)
    t.circle(radius)
    t.end_fill()
layer(150,"OliveDrab",-190)
layer(140,"#873A1B",-180)
layer(120,"#9E3018",-160)
layer(70,"#CC7A1D",-110)
layer(35,"#D99C18",-75)
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
#used to make definitions of layers

def definitions_of_things(sent1,sent2,x,y,Defcolor):
    t.goto(x,y)
    t.color(Defcolor)
    t.write(sent1, font=("Arial", 8, "bold"), align="left")
    t.sety(y-15)
    t.write(sent2, font=("Arial", 8, "bold"), align="left")
definitions_of_things("The lithosphere is the rigid outer layer that includes the crust and the uppermost part of the mantle"," It’s broken into tectonic plates that move slowly over the softer layer beneath.",-500,110,"OliveDrab")
definitions_of_things("The asthenosphere lies just below the lithosphere and is made of partially molten rock that can flow.", "This layer allows the tectonic plates above it to move and shift.",-700,-100,"#873A1B")
definitions_of_things("The mesosphere is the strong, lower part of the mantle beneath the asthenosphere.","It’s made of solid rock that moves more slowly due to higher pressure and density.", -450,-240,"#9E3018")
definitions_of_things("The outer core is a layer of molten iron and nickel surrounding the inner core.", "Its flowing metal creates Earth’s magnetic field.", 75,-240,"#CC7A1D")
definitions_of_things("The inner core is the solid center of the Earth made mostly of iron and nickel.","It remains solid because of the immense pressure at Earth’s center despite extremely high temperatures.", 175,-90,"#D99C18")

screen.exitonclick()