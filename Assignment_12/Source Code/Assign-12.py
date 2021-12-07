########################################################################
##
## CS 101 Lab
## Program Assign-12.py
## Name: Temi Munkhjargal
## Email: tm27m@umsystem.edu
##
## PROBLEM : Using the turtle module we will draw shapes
##
## ALGORITHM : 
##
##      1. Turtle module is imported
##      2. Point class is inititialized and then the draw method is called
##      3. Box class is initialized and the draw function is called
##      4. BoxFilled class is initialized and the draw function is called
##      5. Circle class is initialized and the draw function is called
##      6. FillCircle class is initialized and the draw function is called
##
########################################################################


import turtle
class Point():

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.color(self.color)
        turtle.setheading(0)
        self.draw_action()

    def draw_action(self):
        turtle.dot()


class Box(Point):
    def __init__(self, x1, y1, width, height, color,):
        super().__init__(x1, y1, color)
        self.width = width
        self.height = height
        

    def draw_action(self):
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)
        turtle.right(90)
        turtle.forward(self.width)
        turtle.right(90)
        turtle.forward(self.height)


class BoxFilled(Box):
    def __init__(self, x1, y1, width, height, color, fillcolor):
        self.fillcolor = fillcolor
        super().__init__(x1, y1, width, height, color)

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Box.draw_action(self)
        turtle.end_fill()

class Circle(Point):
    def __init__(self, x1, y1, radius, color):
        super().__init__(x1, y1, color)
        self.radius = radius

    def draw_action(self):
        turtle.circle(self.radius)

class FillCircle(Circle):
    def __init__(self, x1, y1, radius, color, fillcolor):
        super().__init__(x1, y1, radius, color)
        self.fillcolor = fillcolor

    def draw_action(self):
        turtle.fillcolor(self.fillcolor)
        turtle.begin_fill()
        Circle.draw_action(self)
        turtle.end_fill()


p = Point(-100, 100, "blue")
p.draw()

b = Box(-100, 100, 50, 20, "blue")
b.draw()

c = BoxFilled(1, 2, 100, 200, "red", "Blue")
c.draw()

d = Circle(-50, 50, 60, "red")
d.draw()

a = FillCircle(-200, 75, 90, "red", "green")
a.draw()
