import turtle
import random

colors = ['red','green','blue','black','white','brown','yellow']
screen = turtle.Screen()

def make_turtles(num):
    res = []
    for cnt in range(num):
        x = turtle.Turtle()
        x.color(random.choice(colors))
        x.right(random.randint(0, 360))
        x.forward(random.randint(1, 100))
        res.append(x)
    return res


if __name__ == '__main__':
    make_turtles(10)
    screen.exitonclick()
