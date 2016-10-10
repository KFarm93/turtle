from turtle import *


def triangle(size):
    for i in range(3):
        forward(size)
        left(120)
            

def square(size):
    for i in range(4):
        forward(size)
        left(90)

def pentagon(size):
    for i in range(5):
        forward(size)
        left(72)

def hexagon(size):
    for i in range(6):
        forward(size)
        left(60)

def octagon(size):
    for i in range(8):
        forward(size)
        left(45)

def star(size):
    for i in range(5):
        left(size)
        forward(100)

def circle():
    for i in xrange(360):
        forward(1)
        left(1)
