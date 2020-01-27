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
		self.size = size

		self.puzzle = self.puzzle_solving[0]
		self.puzzle_solving.pop()
		self.print_puzzle()
		self.bind('<Button-1>', self.button_handler)

    # def create_widgets(self):
    #     self.hi_there = tk.Button(self)
    #     self.hi_there["text"] = "Hello World\n(click me)"
    #     self.hi_there["command"] = self.say_hi
    #     self.hi_there.pack(side="top")

    #     self.quit = tk.Button(self, text="QUIT", fg="red",
    #                           command=self.master.destroy)
    #     self.quit.pack(side="bottom")

    # def say_hi(self):
    #     print("hi there, everyone!")
	def button_handler(self, button=None):
		if self.puzzle_solving != []:
			self.puzzle = self.puzzle_solving.pop()
			self.print_puzzle()
		else:
			exit(0)


	def print_puzzle(self):
		self.delete("all")
		for i in range(len(self.puzzle)):
			if self.puzzle[i] == 0:
				color = "white"
			else:
				color = "red"
			top_left = Point(100 * (i % self.size), 100 * (i // self.size))
			botto_right = Point(100 + 100 * (i % self.size), 100 + 100 * (i // self.size))
			self.create_rectangle(top_left.x, top_left.y, botto_right.x, botto_right.y, fill=color)
			self.create_text((50 + top_left.x, 50 + top_left.y), text=self.puzzle[i], font="Verdana 40")
		self.pack(fill=BOTH, expand=1)


if __name__ == "__main__":
	root = Tk()

	size = 3

	# c = tk.Canvas(root, height=size * 100, width=size * 100, bg='white')
	# c.pack(fill=tk.BOTH, expand=True)

	#app = Visualization(master=root, size=size)
	#app.mainloop()