#! /usr/bin/env python
"""Proyecto CC471 - Analisis Bioinformatico de Especies
"""

import os
import sys

# import Bio
import tkinter as tk
# from Bio.Seq import Seq

win = tk.Tk()

win.title("Proyecto CC471 - Analisis Bioinformatico de Especies")
tk.Label(win, text="Label 1").grid(column=0,row=0)
a_label = tk.Label(win, text = "Another Label")
a_label.grid(column=1,row=0)

def click_me():
    """Funcion que crea un boton
    """
    action.configure(text="** He sido apretado! **")
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

action = tk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1,row=1)

win.mainloop()
