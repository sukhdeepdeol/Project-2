import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create a turtle for drawing
land = turtle.Turtle()
land.speed(3)

# Function to draw ground
def draw_ground():
    land.penup()
    land.goto(-400, -100)
    land.pendown()
    land.color("chocolate")
    land.begin_fill()
    for _ in range(2):
        land.forward(800)
        land.right(90)
        land.forward(200)
        land.right(90)
    land.end_fill()

# Function to draw a tree
def draw_tree(x, y):
    # Draw the trunk
    land.penup()
    land.goto(x, y)
    land.pendown()
    land.color("saddlebrown")
    land.begin_fill()
    for _ in range(2):
        land.forward(20)
        land.left(90)
        land.forward(40)
        land.left(90)
    land.end_fill()

    # Draw the leaves
    land.penup()
    land.goto(x - 15, y + 35)
    land.pendown()
    land.color("forestgreen")
    land.begin_fill()
    land.circle(25)
    land.end_fill()

# Function to draw the sun
def draw_sun():
    land.penup()
    land.goto(150, 150)
    land.pendown()
    land.color("yellow")
    land.begin_fill()
    land.circle(40)
    land.end_fill()

# Draw the landscape
draw_ground()
draw_tree(-100, -100)
draw_tree(50, -130)
draw_tree(200, -100)
draw_sun()

# Hide the turtle and finish
land.hideturtle()
turtle.done()
