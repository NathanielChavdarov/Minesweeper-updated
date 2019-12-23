from tkinter import Tk, Frame, Button, Canvas
import random
import numpy as np

GRIDWIDTH=4
GRIDHEIGHT=4

root = Tk()
root.title("MineSweeper")

c = Canvas(root, width=350, height=350, bg='white')
c.pack()

f = Frame(root, height="350", width="350", bd=2)
f.pack()

for x in range(GRIDWIDTH):
    for y in range(GRIDHEIGHT):
        b = Button(c, height=5, width=5)
        b.grid(row=x, column=y)

grid = np.array([
    [
    random.randint(0, 1) for x in range(GRIDWIDTH)
    ]
    for y in range(GRIDHEIGHT)
    ])

root.mainloop()
