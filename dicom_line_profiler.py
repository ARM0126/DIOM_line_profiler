#import numpy as np
import matplotlib.pyplot as plt
#import mplcursors
import pydicom
#from reportlab.lib.pagesizes import letter
#from reportlab.pdfgen import canvas
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QLabel
import sys
import traceback


try:
    # your entire program code here
    class MyApp(QWidget):
        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            self.setGeometry(100, 100, 500, 500)
            self.setWindowTitle('Line Profile App')

            label = QLabel('Drag and drop DICOM image here', self)
            label.move(50, 50)
            label.resize(400, 100)

            self.show()

            self.setAcceptDrops(True)

        def dragEnterEvent(self, event):
            if event.mimeData().hasUrls():
                event.accept()
            else:
