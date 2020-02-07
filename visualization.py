from tkinter import *
import time

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Visualization(Canvas):
    def __init__(self, puzzle_solving, size, master=None, bg="white"):
        super().__init__(master, height=size * 100, width=size * 100, bg=bg)
        self.master = master
        self.puzzle_solving = puzzle_solving
        self.puzzle_solving.reverse()
        self.size = size

        self.auto = True
        self.index = 0
        self.print_puzzle(puzzle_solving[self.index])
        self.master.bind('<Left>', self.left_button_handler)
        self.master.bind('<Right>', self.right_button_handler)
        self.master.bind('<Button-1>', self.button_handler)


    def left_button_handler(self, button=None):
        self.auto = False
        if self.index - 1 >= 0:
                self.index -= 1
        self.print_puzzle(self.puzzle_solving[self.index])


    def right_button_handler(self, button=None):
        self.auto = False
        if self.index + 1 < len(self.puzzle_solving):
                self.index += 1
        self.print_puzzle(self.puzzle_solving[self.index])


    def button_handler(self, button=None):
        if button is not None:
            self.auto = True
        if self.index + 1 < len(self.puzzle_solving):
            self.index += 1
        else:
            return
        self.print_puzzle(self.puzzle_solving[self.index])
        if self.auto:
            self.master.after(200, self.button_handler)

    def print_puzzle(self, puzzle):
        self.delete("all")
        for i in range(len(puzzle)):
            if puzzle[i] == 0:
                color = "white"
            else:
                color = "red"
            top_left = Point(100 * (i % self.size), 100 * (i // self.size))
            botto_right = Point(100 + 100 * (i % self.size), 100 + 100 * (i // self.size))
            self.create_rectangle(top_left.x, top_left.y, botto_right.x, botto_right.y, fill=color)
            self.create_text((50 + top_left.x, 50 + top_left.y), text=puzzle[i], font="Verdana 40")
        self.pack(fill=BOTH, expand=1)
