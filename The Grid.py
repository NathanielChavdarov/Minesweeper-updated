from tkinter import *

btns = [
    (lambda ctl: ctl.grid(row=r, column=c) or ctl)(
        Button())
    for c in (0,1,2,3,4,5,6,7,8,9,10,11) for r in (0,1,2,3,4,5,6,7,8,9,10,11)]