from processing import *

x = 0

def setup():
    size(800,500)

def draw():
    global x

    background(255)
    circle(x,250,50)

    x += 2

run()