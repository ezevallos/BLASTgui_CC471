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
tk.Label(win, text = "Entra secuencia: ").grid(column=0,row=0)
a_label = tk.Label(win, text = "Aqui")
a_label.grid(column=1,row=0)

def click_me():
    """Funcion que pide secuencia
    """
    action.configure(text="** Leemos la secuencia **"+ name.get())
    a_label.configure(foreground='red')
    a_label.configure(text='Excelente secuencia')

action = tk.Button(win,text="Procesar", command=click_me)
action.grid(column=1,row=1)

name = tk.StringVar()
name_entered = tk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0,row=1)

win.mainloop()
