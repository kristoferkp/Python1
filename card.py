import turtle
from random import randint

turtle.screensize(600, 600)
turtle.bgcolor("lightblue")

def draw_triangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(3):
        t.forward(length)
        t.left(120)
    t.end_fill()

def draw_tree(t, start_size, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(3):
        draw_triangle(t, start_size, "green")
        t.penup()
        t.right(90)
        t.forward(start_size - start_size/2)
        t.left(90)
        t.pendown()
    t.penup()
    t.left(90)
    t.forward(start_size - start_size/2)
    t.right(90)
    t.forward(start_size*0.4)
    t.pendown()
    draw_rectangle(t, start_size*0.2, "brown")


def draw_rectangle(t, length, color):
    t.fillcolor(color)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(length*2)
        t.right(90)
    t.end_fill()

def draw_circle(t, radius, color):
    t.fillcolor(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_snowman():
    snowman = turtle.Turtle()
    snowman.speed(0)
    snowman.penup()
    snowman.goto(0, -200)  # Position the turtle at the bottom of the screen
    snowman.pendown()

    # Draw the body of the snowman
    for radius, color in [(40, "white"), (30, "white"), (20, "white")]:
        draw_circle(snowman, radius, color)
        snowman.penup()
        snowman.left(90)
        snowman.forward(radius*2)
        snowman.right(90)
        snowman.pendown()
    
    # Draw the eyes
    snowman.penup()
    snowman.goto(-8, -40)
    snowman.pendown()
    draw_circle(snowman, 3, "black")
    snowman.penup()
    snowman.goto(8, -40)
    snowman.pendown()
    draw_circle(snowman, 3, "black")

    # Draw the nose
    snowman.penup()
    snowman.goto(-3, -48)
    snowman.pendown()
    draw_triangle(snowman, 10, "orange")

    # Draw the buttons
    snowman.penup()
    snowman.goto(0, -80)
    snowman.pendown()
    for i in range(3):
        draw_circle(snowman, 3, "black")
        snowman.penup()
        snowman.right(90)
        snowman.forward(15)
        snowman.left(90)
        snowman.pendown()



    snowman.hideturtle()


# Create a turtle to draw the tree
tree_turtle = turtle.Turtle()
tree_turtle.speed(0)

# Calculate the number of trees and the spacing between them
num_trees = 15
x_spacing = 800 // num_trees  # Assuming the total available x-space is 800 units

for i in range(num_trees):
    x = -400 + i * x_spacing  # Calculate the x-coordinate for each tree
    y = randint(-200, 300)  # Keep the y-coordinate random
    draw_tree(tree_turtle, 120, x, y)

tree_turtle.hideturtle()

message_turtle = turtle.Turtle()
message_turtle.penup()
message_turtle.goto(-150, -300)
message_turtle.pendown()
message_turtle.color("white")
message_turtle.write("Häid jõule!", font=("Roboto", 48, "bold"))
message_turtle.hideturtle()


draw_snowman()

turtle.done()