from turtle import Turtle, Screen

window = Screen()
window.setup(1000, 600)
window.bgcolor("black")

sam = Turtle()
sam.pensize(3)
sam.color("white")
sam.shape("turtle")
sam.speed("fastest")

def draw_circle():
  sam.penup()
  sam.goto(-350, -150)
  sam.pendown()
  for _ in range(10):
    sam.circle(50)
    sam.left(360 / 10)
    

def draw_square():
  sam.penup()
  sam.goto(0,0)
  sam.pendown()
  for _ in range(10):
    for _ in range(4):
      sam.forward(100)
      sam.left(90)
    sam.left(360 / 10)

def draw_star():
  sam.penup()
  sam.goto(350, 150)
  sam.pendown()
  for _ in range(10):
    sam.forward(100)
    sam.left(45)
    sam.forward(50)
    sam.left(135)
    sam.left(360 / 10)

def draw_traingle():
  sam.penup()
  sam.goto(350, 150)
  sam.pendown()
  for _ in range(10):
    for _  in range(3):
      sam.forward(100)
      sam.left(120)
    sam.left(360 / 10)


draw_circle()
draw_square()
#draw_star()
draw_traingle()

window.exitonclick()