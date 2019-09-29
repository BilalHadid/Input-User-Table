# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 01:13:40 2019

@author: bilal
"""

import tkinter as tk
import tkinter as ttk
root = tk.Tk()
root.title("Sir Task")

root.wm_geometry("250x200")

lbl = ttk.Label(root, text = "Enter the name:").grid(column = 0, row = 0)  


def write_slogan():
   for x in range(1,11,1):

    print(name.get(),"+",x,"=",(name.get()*x))



name = tk.IntVar()
nameEntered = ttk.Entry(root,
                       width = 25,
                       textvariable = name).grid(column = 0, row = 1)  

button = ttk.Button(root,
                   text = "submit",
                   command = write_slogan).grid(column = 0, row = 3) 


root.mainloop()