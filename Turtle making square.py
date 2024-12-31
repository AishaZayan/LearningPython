from turtle import Turtle, Screen

sam = Turtle("turtle")
#sam.shape("turtle")
sam.color("blue")
for _ in range(3):
  sam.forward(100)
  sam.left(90)


window = Screen()
window.exitonclick()