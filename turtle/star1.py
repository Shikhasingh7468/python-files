from turtle import *
color("blue","black")
begin_fill()
while True:
    forward(200)
    shape('turtle')
    left(170)
    # shapesize(3,3,3)
    if abs(pos()) <1:
        break
end_fill()
done()