from turtle import Turtle, Screen

sam = Turtle("turtle")
sam.color("DarkSeaGreen4")
for _ in range(3):
  sam.forward(100)
  sam.left(120)
  
window = Screen()

window.exitonclick()