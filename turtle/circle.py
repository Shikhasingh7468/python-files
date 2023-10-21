import turtle 
t = turtle.Turtle() 
t.pen(pencolor="red", fillcolor="blue", pensize=10, speed=3)

t.begin_fill() # Start filling
t.circle(100) # Radius of a circle
t.end_fill()
turtle.done()