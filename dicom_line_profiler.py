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
                event.ignore()

        def dropEvent(self, event):
            for url in event.mimeData().urls():
                path = url.toLocalFile()
                if path.endswith('.dcm'):
                    self.process_image(path)
                else:
                    print('Invalid file type, please drop a DICOM image')

        def process_image(self, path):
            global ds, fig, fig2, ax0, ax1, marker

            ds = pydicom.dcmread(path)

            # create a figure with two subplots for the line profiles
            fig2, (ax0, ax1) = plt.subplots(ncols=2, figsize=(10, 5))
            ax0.set_title('Line profile X')
            ax1.set_title('Line profile Y')
            ax0.set_xlabel('Pixel Number')
            ax1.set_xlabel('Pixel Number')
            ax0.set_ylabel('Pixel Value')
            ax1.set_ylabel('Pixel Value')

            fig2.savefig("line_profiles.png")

            # plot the DICOM image
            fig = plt.figure(figsize=(5, 5))
            plt.imshow(ds.pixel_array, cmap='gray')
            plt.axis('off')

            # add a marker to select a point for the line profile
            marker, = plt.plot([], [], 'r+', markersize=10)
            # add a click event handler to the image
            cid = fig.canvas.mpl_connect('button_press_event', onclick)

            # create the marker on the DICOM image
            fig, ax = plt.subplots()
            ax.imshow(ds.pixel_array, cmap=plt.cm.gray)
            marker = ax.plot([], [], marker="o", color="r")
            fig.canvas.mpl_connect("button_press_event", onclick)

            # create a button to save the resulting profile plots and DICOM image to a PDF document
            button_ax = plt.axes([0.8, 0.05, 0.15, 0.075])
            button = plt.Button(button_ax, "Save to PDF")
            button.on_clicked(save_to_pdf)

            # show the plots
            plt.show()


    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = MyApp()
        sys.exit(app.exec_())

except:
    print("Exception occurred:")
    print(traceback.format_exc())
    sys.exit(1)
