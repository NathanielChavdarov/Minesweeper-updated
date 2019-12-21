from tkinter import *
import random
import numpy as np

GRIDWIDTH = 4
GRIDHEIGHT = 4

grid = np.array([
    [
    random.randint(0, 1) for x in range(GRIDWIDTH)
    ]
    for y in range(GRIDHEIGHT)
    ])

print(grid)
