# DIOM_line_profiler
A lightweight PyQt5 app to load DICOM `.dcm` images, click a point, and extract X/Y line profiles across that point.



This script:

Uses PyQt5 for a GUI that accepts drag-and-drop of DICOM files.

Loads and displays a DICOM image using pydicom and matplotlib.

Lets the user click on the image to generate line profiles in X and Y directions (see screenshot below).

Has a button to save plots to a PDF using reportlab.

Includes exception handling and application cleanup.

![DIOCM Profile plotter](dicom line profiler screen.png) 
![DIOCM Profile plotter](Hexatic.png)
