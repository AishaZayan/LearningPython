from turtle import Turtle, Screen
import random

window = Screen()
window.setup(1000, 600)
window.bgcolor("black")

sam = Turtle()
sam.shape("turtle")
sam.color("white")
sam.pensize(5)
sam.speed("fast")

tom = Turtle()
tom.shape("turtle")
tom.color("orange")
tom.pensize(5)
tom.speed("fast")

random_angles = [0,90,180,270]
random_distant = [20,30,40,50,60,708,0,90,100]
loop_count = [5,10,15,20,25,30]

def draw_random(turtle_name):
  for _ in range(random.choice(loop_count)):
    turtle_name.forward(random.choice(random_distant))
    turtle_name.left(random.choice(random_angles))

for _ in range(20):
  tom.circle(100)
  tom.left(360 / 20)

draw_random(sam)

window.exitonclick()
