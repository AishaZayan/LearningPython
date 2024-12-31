from turtle import Turtle,Screen

sam = Turtle("classic")
sam.color("CornflowerBlue")
sam.speed("slowest")

sam.penup()
sam.forward(100)
sam.pendown()
sam.pensize(10)
sam.circle(100)
#sam.speed("fastest")
#for _ in range(360):
#  sam.forward(1)
#  sam.left(1)

window = Screen()
window.exitonclick()