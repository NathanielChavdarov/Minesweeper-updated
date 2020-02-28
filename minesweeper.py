import tkinter
import random
from typing import Callable

GRIDWIDTH = 6
GRIDHEIGHT = 6
NUMBEROFMINES = 5

global WinOrNot
WinOrNot = False

root = tkinter.Tk()
root.title("MineSweeper")

canvas = tkinter.Canvas(root, width=500, height=500, bg='black')
canvas.pack()

frame = tkinter.Frame(canvas, height=450, width=450, bd=2)
frame.pack()

firstClick = False

buttons = [
    [
        None for x in range(GRIDWIDTH)
    ]
    for y in range(GRIDHEIGHT)
]

buttonTextVariable = [
    [
        tkinter.StringVar() for x in range(GRIDWIDTH)
    ]
    for y in range(GRIDHEIGHT)
]


def makeMines(safex, safey, minesnum):
    q = [
        [
            0 for x in range(GRIDWIDTH)
        ]
        for y in range(GRIDHEIGHT)
    ]
    for i in range(minesnum):
        randX = safex
        randY = safey

        while (randX, randY) == (safex, safey) or q[randY][randX] == 1:
            randX = random.randint(0, GRIDWIDTH-1)
            randY = random.randint(0, GRIDHEIGHT-1)
        q[randY][randX] = 1
    # print("\n".join(
    #     " ".join(
    #         str(col) for col in row
    #     )
    #     for row in q
    # ))
    return q

def returnMineNum(x: int, y:int) -> str:
    if safeUnsafe[y][x] == 1:
        return "M"
    adjacent = 0
    # right
    if x < GRIDWIDTH-1 and safeUnsafe[y][x+1] == 1:
        adjacent = adjacent + 1
    #left
    if x-1 > 0 and safeUnsafe[y][x-1] == 1:
        adjacent = adjacent + 1
    #above
    if y < GRIDHEIGHT-1 and safeUnsafe[y+1][x] == 1:
        adjacent = adjacent + 1
    #below
    if y-1 > 0 and safeUnsafe[y-1][x] == 1:
        adjacent = adjacent + 1
    #aboveright
    if x < GRIDWIDTH-1 and y < GRIDHEIGHT-1 and safeUnsafe[y+1][x+1] == 1:
        adjacent = adjacent + 1
    #aboveleft
    if x-1 > 0 and y < GRIDHEIGHT-1 and safeUnsafe[y+1][x-1] == 1:
        adjacent = adjacent + 1
    #belowright
    if x < GRIDWIDTH-1 and y-1 > 0 and safeUnsafe[y-1][x+1] == 1:
        adjacent = adjacent + 1
    #belowleft
    if x-1 > 0 and y-1 > 0 and safeUnsafe[y-1][x-1] == 1:
        adjacent = adjacent + 1
    return str(adjacent)


def onlyminesleft():
    numOfEmptyButtons = 0
    for y in range(GRIDHEIGHT):
        for x in range(GRIDWIDTH):
            if buttonTextVariable[y][x].get() == "":
                numOfEmptyButtons = numOfEmptyButtons + 1
    if numOfEmptyButtons == NUMBEROFMINES:
        print("You Win")
        root.destroy()
        exit(0)


def nearMineCheck(x: int, y: int) -> str:
    #check grid points to the right
    for i in range(x, GRIDWIDTH):
        gridPointText = returnMineNum(i, y)
        if gridPointText == "M":
            break
        buttonTextVariable[y][i].set(gridPointText)
    #check grid points above
    for j in range(y+1, GRIDHEIGHT):
        gridPointText = returnMineNum(x, j)
        if gridPointText == "M":
            break
        buttonTextVariable[j][x].set(gridPointText)
    #check grid points below
    for j in range(y-1, -1, -1):
        gridPointText = returnMineNum(x, j)
        if gridPointText == "M":
            break
        buttonTextVariable[j][x].set(gridPointText)
    #check grid points to the left
    for i in range(x-1, -1, -1):
        gridPointText = returnMineNum(i, y)
        if gridPointText == "M":
            break
        buttonTextVariable[y][i].set(gridPointText)


def hasText(x: int, y: int) -> bool:
    gotText = False
    if buttonTextVariable[y][x].get() != "":
        gotText = True

    return gotText



def buttonPress(x: int, y: int) -> None:
    """
    A function to be called when a button is pressed
    """
    global firstClick
    global safeUnsafe
    if not firstClick:
        firstClick = True
        safeUnsafe = makeMines(x, y, NUMBEROFMINES)
        nearMineCheck(x, y)
        return
    if safeUnsafe[y][x] == 1:
        print("game over!")
        root.destroy()
        exit(0)

    if hasText(x, y) != True:
        nearMineCheck(x, y)
    else:
        print(" ")
    onlyminesleft()


def generateFunction(aa: int, bb: int) -> Callable[[], None]:
    """
    This function takes two arguments, aa and bb. It returns a function which
    takes zero arguments, but knows aa and bb because theses two variables are
    in scope.
    """
    # Create a function called wibble, which takes zero arguments, but knows aa
    # and bb because they are in scope.
    def wibble() -> None:
        buttonPress(aa, bb)

    # Return the function we just created.
    return wibble


for y in range(GRIDHEIGHT):
    for x in range(GRIDWIDTH):
        bp = generateFunction(x, y)
        b = tkinter.Button(
            frame, width=1, height=1, textvariable=buttonTextVariable[y][x],
            command=bp).grid(row=y, column=x)
        # func11 = generateFunction(x, y)
        buttons[y][x] = b

root.mainloop()
