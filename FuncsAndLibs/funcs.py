from turtle import *
from sympy import *
import turtle
from random import randint

class Drawer():
    def __init__(self):
        self.t = None
        self.colors = ["Red", "Green", "Blue"]
        self.is_drawn_grid = False
    
    def draw_grid(self):
        self.t = turtle.Turtle()
        turtle.setup(width = 700, height = 700)
        self.t.penup()
        self.t.setx(-1920)
        self.t.pendown()
        self.t.speed(100)
        self.t.pensize(3)
        self.t.setposition(1920, 0)
        #t.goto(-1920, 0)
        self.t.setposition(0, 1200)
        self.t.goto(0, -1200)
        self.t.penup()
        self.t.setx(-1920)
        self.t.sety(-1200)
        self.t.pendown()

        self.t.pensize(0.3)
        
        y = -1200
        """
        for i in range(100):
            self.t.goto(1920, y)
            self.t.penup()
            self.t.goto(-1920, y)
            self.t.pendown()
            y+=100
            
        x = -1920
        
        for i in range (100):
            self.t.goto(x, 1200)
            self.t.penup()
            self.t.goto(x, -1200)
            self.t.pendown()
            x+=100
        """
    def calc_func(self, str_expr):
        list_x = []
        list_y = []

        x = symbols("x")

        expr = sympify(str_expr)

        i = -10
        
        while (i < 10):
            list_x.append(i)
            i += 0.1
            
        for i in range(len(list_x)):
            list_y.append(expr.subs(x, list_x[i]))

        return (list_x, list_y)

    def draw_func(self, str_expr):
        if not self.is_drawn_grid:
            self.draw_grid()
            self.is_drawn_grid = True
        self.t.pensize(3)
        coords = self.calc_func(str_expr)
        self.t.penup()
        self.t.color(self.colors[randint(0, 2)])
        self.t.goto(coords[0][0]*100, coords[1][0]*100)
        self.t.pendown()
        for i in range(len(coords[0])):
            self.t.goto(coords[0][i]*100, coords[1][i]*100)










