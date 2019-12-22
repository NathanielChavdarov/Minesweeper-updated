import tkinter
import random
import numpy as np

GRIDWITH=4
GRIDHEIGHT=4

root = tkinter.Tk()
root.geometry('350x350')
root.title("MineSweeper")

f = Frame(root, bd=2, height=345, width=345, bg="white")
f.pack()

c = Canvas(root, width=300, height=300)
c.pack()

buttons = np.array([
    [
    Button(root, height=10, width=10, bg="green") for x in range(GRIDWIDTH)
    ]
    for y in range(GRIDHEIGHT)
    ]
    )

grid = np.array([
    [
    random.randint(0, 1) for x in range(GRIDWIDTH)
    ]
    for y in range(GRIDHEIGHT)
    ])

print(grid)
