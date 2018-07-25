from tkinter import *
from sympy import *
from turtle import *
from FuncsAndLibs.funcs import *

class App():
    def draw(self, str_expr):
        self.drawer.draw_func(str_expr)
        
    def __init__(self):
        self.drawer = Drawer()
        self.result = 0
        self.root = Tk()
        self.label = Label(text = "Expression: ")
        self.text = Text(width = 30, height = 1)
        self.btn1 = Button(self.root, text = "Draw", command = lambda: self.draw(self.text.get("0.0", END)))
        self.label.pack()
        self.text.pack()
        self.btn1.pack()
        self.root.mainloop()

app = App()
