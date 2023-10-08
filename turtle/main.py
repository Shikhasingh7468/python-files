import turtle

gp = turtle.Turtle() # Default Turtle Object (classic black pointer)

print(f"Shape:{gp.shape()}") # Returns current shape of object

screen = turtle.Screen()
screen.title("Python Turtle")
screen.bgcolor('black') # Change the bg from white to black


gp.shape('turtle') # Change the shape to turtle
gp.color('green') # Change the color to green
gp.forward(100) # Move object forwand by 100 pixels

turtle.done() # Mera ho gaya