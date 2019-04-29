#! /usr/bin/env python
"""Proyecto CC471 - Analisis Bioinformatico de Especies
"""

import os
import sys
import plotly.plotly as py
import plotly.figure_factory as ff
import Bio
from PyQt4 import QtGui
from Bio.Seq import Seq

def window():
 app = QtGui.QApplication(sys.argv)
 w = QtGui.QWidget()
 b= QtGui.QLabel(w)
 b.setText("Aquí construimos nuestra app!")
 w.setGeometry(100,100,200,50)
 b.move(50,20)
 w.setWindowTitle(“Proyecto CC471 - Análisis Bioinformático de Especies”)
 w.show()
 sys.exit(app.exec_())
if __name__ == '__main__':
 window()
