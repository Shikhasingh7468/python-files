import turtle

screen = turtle.Screen()

screen.title("Ruchiii")


ruchi_turtle = turtle.Turtle()


ruchi_turtle.penup()
ruchi_turtle.goto(0, 0)
ruchi_turtle.pendown()
ruchi_turtle.write("Ruchiii", align="center", font=("Arial", 28, "normal"))

screen.exitonclick()