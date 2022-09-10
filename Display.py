#!/usr/bin/env python3

'''
USE TO DISPLAY THE GAME. IN PROG
'''
from tkinter import *

class Display:
    def __init__(self):
        win = Tk()
        win.geometry('1080X1080')
        label=Label(win, text="", font=("Courier 22 bold"))
        label.pack()
        entry= Entry(win, width= 40)
        entry.focus_set()
        entry.pack()