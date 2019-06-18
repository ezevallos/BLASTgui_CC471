#! /usr/bin/env python
"""Proyecto CC471 - Analisis Bioinformatico de Especies
"""

from Bio import SeqIO
from Bio import AlignIO
from Bio.Align import AlignInfo
from Bio import SubsMat
from Bio.Align.Applications import ClustalwCommandline


import tkinter as tk
from tkinter import *
from tkinter import Menu
import os, sys

path = 'Secuencias/.'
dirs = os.listdir(path)

for file in dirs:
    print(file)


#############
# funciones #
#############

# Alinea los archivos en la lista files
# contenidos en la carpeta folderName
def alignFunction(folderName, files, tkWindow) :

	records = []
	for filename in files :
		handle = open(folderName + "/" + filename)
		record = SeqIO.read( handle, "swiss" )
		records.append ( record )
	SeqIO.write(records, "TOALIGN.fasta", "fasta")	
	cline = ClustalwCommandline("clustalw2", infile="TOALIGN.fasta")
	
	window = Toplevel(tkWindow)
	window.title("Alineamiento")
	canvas = Canvas(window, width=800, height=650, bg = '#afeeee')

	cline()
	alignment = AlignIO.read(open("TOALIGN.aln"), "clustal")
	summary_align = AlignInfo.SummaryInfo(alignment)
	consensus = summary_align.dumb_consensus()

	canvas.create_text(10,10, anchor=NW,fill="darkblue",font="Courier 12", text=str(alignment))
	canvas.pack()
	window.mainloop()
	return

# funcion ayudadora, invocada con el boton ALINEAR
# distingue los checkboxes activos, y segun eso
# llama a alignFunction

def aligner(folderName, files, checks, tkWindow) :
	alignNames = []
	i = 0
	
	for name in files :
		if checks[i].get() == 1 :
			alignNames.append(name)
		i = i + 1
	
	alignFunction(folderName, alignNames, tkWindow)
	return

# crea una ventana con checkboxes para alinear 
# los archivos contenidos en la carpeta folder

def checkWindow(folder, tkWindow) :
	window = Toplevel(tkWindow)
	window.title("Alineamiento - Seleccion carpeta : " + folder)

	files = os.listdir(folder)

	checks = []

	i = 0

	for file in files :
		checks.append(IntVar())
		Checkbutton(window, text=file, variable=checks[i]).grid(column= i//20 + 1, row=(i%20)+1, sticky=W)
		print(file)
		i = i + 1

	Button(window, text='ALINEAR', command=lambda : aligner(folder, files, checks, window)).grid(column= i//20 + 1, row=(i%20)+1, sticky=W)

	window.mainloop()
	return

win = tk.Tk()

win.title("Proyecto CC471 - Analisis Bioinformatico de Especies")
tk.Label(win, text="Entre nombre de carpeta: ").grid(column=0, row=0)
a_label = tk.Label(win, text="Aqui")
a_label.grid(column=1, row=0)


def click_me():
    """Funcion que pide secuencia
    """
    action.configure(text="** Leemos la carpeta **" + name.get())

    a_label.configure(foreground="red")
    a_label.configure(text="Excelente secuencia")
    checkWindow(name.get(), win)

name = tk.StringVar()
name_entered = tk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = tk.Button(win, text="Procesar", command=click_me)
action.grid(column=1, row=1)

win.mainloop()
