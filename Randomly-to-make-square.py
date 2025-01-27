from turtle import Turtle, Screen
import random

sam = Turtle()
sam.speed("slowest")
colors = ["black", "white", "midnight blue", "lime", "alice blue", "brown", "hot pink", "navajo white", "dark violet", "orange", "dark red"]
shapes = ["classic", "turtle", "square", "circle", "arrow"]
size = [2,4,6,8,10,12]




def draw_square():
  for _ in range(4):
    sam.color(random.choice(colors))
    sam.shape(random.choice(shapes))
    sam.pensize(random.choice(size))
    sam.forward(100)
    sam.left(90)

draw_square()

window = Screen()
window.exitonclick()