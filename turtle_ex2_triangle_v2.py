from turtle import *

def triangle(size, fill, color):
    if fill == "yes":
        begin_fill()
    for i in range(3):
        forward(size)
        left(120)
    end_fill()

triangle(200, "yes", color("red", "green"))

mainloop()
