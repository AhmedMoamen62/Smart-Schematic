# import required library for GUI
from PySide2.QtWidgets import QApplication,QWidget,QLabel
from PySide2.QtGui import QIcon,QPixmap,QFont,QMouseEvent
from PySide2.QtCore import Qt
from PySide2 import QtGui

# import sys to run the application
import sys

class Window(QWidget):
    def __init__(self):
        # call the constructor of the parent (QWidget)
        super().__init__()

        # check if it the first time for user to plot
        self.firstTime = False

        # set title for the window
        self.setWindowTitle("Smart Schematic")

        # add the schematic to the widget and center it
        self.label = QLabel(self)
        self.pixmap = QPixmap('schematic.png')
        self.pixmap = self.pixmap.scaled(self.pixmap.width()*0.7,self.pixmap.height()*0.7,Qt.KeepAspectRatio)
        self.label.setPixmap(self.pixmap)
        self.label.setScaledContents(True)
        self.resize(self.pixmap.width(), self.pixmap.height())

        # set minimum width and height for the window to fit the image
        self.setMinimumHeight(self.pixmap.height())
        self.setMinimumWidth(self.pixmap.width())
        self.setMaximumHeight(self.pixmap.height())
        self.setMaximumWidth(self.pixmap.width())

        # set icon for the application at run time and center the application window with the primary screen
        self.setIcon()
        self.center()

        # add default transistors label for the schematic
        self.setTransistorsLabels()

        # add default components label for the schematic
        self.setFixedLabels()

    # add all transistors label at the start above the schematic
    def setTransistorsLabels(self):
        # set default font for all transistors label
        font = QFont("SansSerif",13,italic=True)

        # set all transistors label
        self.trans1a = QLabel(self.label)
        self.trans1a.setText("M1a")
        self.trans1a.move(282,245)
        self.trans1a.setFont(font)

        self.trans2a = QLabel(self.label)
        self.trans2a.setText("M2a")
        self.trans2a.move(80,368)
        self.trans2a.setFont(font)

        self.trans3a = QLabel(self.label)
        self.trans3a.setText("M3a")
        self.trans3a.move(80,288)
        self.trans3a.setFont(font)

        self.trans4a = QLabel(self.label)
        self.trans4a.setText("M4a")
        self.trans4a.move(80,178)
        self.trans4a.setFont(font)

        self.trans5a = QLabel(self.label)
        self.trans5a.setText("M5a")
        self.trans5a.move(80,110)
        self.trans5a.setFont(font)

        self.trans1b = QLabel(self.label)
        self.trans1b.setText("M1b")
        self.trans1b.move(342, 245)
        self.trans1b.setFont(font)

        self.trans2b = QLabel(self.label)
        self.trans2b.setText("M2b")
        self.trans2b.move(545, 368)
        self.trans2b.setFont(font)

        self.trans3b = QLabel(self.label)
        self.trans3b.setText("M3b")
        self.trans3b.move(545, 288)
        self.trans3b.setFont(font)

        self.trans4b = QLabel(self.label)
        self.trans4b.setText("M4b")
        self.trans4b.move(545, 178)
        self.trans4b.setFont(font)

        self.trans5b = QLabel(self.label)
        self.trans5b.setText("M5b")
        self.trans5b.move(545, 110)
        self.trans5b.setFont(font)

        self.colorDefaultLabels()

    # color all transistors with blue
    def colorDefaultLabels(self):
        self.trans1a.setStyleSheet("color: blue")
        self.trans2a.setStyleSheet("color: blue")
        self.trans3a.setStyleSheet("color: blue")
        self.trans4a.setStyleSheet("color: blue")
        self.trans5a.setStyleSheet("color: blue")

        self.trans1b.setStyleSheet("color: blue")
        self.trans2b.setStyleSheet("color: blue")
        self.trans3b.setStyleSheet("color: blue")
        self.trans4b.setStyleSheet("color: blue")
        self.trans5b.setStyleSheet("color: blue")

    def setFixedLabels(self):
        # set default fonts for all components label
        font1 = QFont("SansSerif", 13, italic=True)
        font2 = QFont("SansSerif", 10, italic=True)
        font3 = QFont("SansSerif", 8, italic=True)

        label1 = QLabel(self.label)
        label1.setText("Vcascn")
        label1.move(185, 300)
        label1.setFont(font1)

        label2 = QLabel(self.label)
        label2.setText("Vin+")
        label2.move(185, 255)
        label2.setFont(font1)

        label3 = QLabel(self.label)
        label3.setText("Vout-")
        label3.move(41, 245)
        label3.setFont(font1)

        label4 = QLabel(self.label)
        label4.setText("Vcascp")
        label4.move(185, 183)
        label4.setFont(font1)

        label5 = QLabel(self.label)
        label5.setText("Vcmfp")
        label5.move(226, 103)
        label5.setFont(font1)

        label6 = QLabel(self.label)
        label6.setText("Vbiasp")
        label6.move(226, 103)
        label6.setFont(font1)

    # set icon for the application
    def setIcon(self):
        appIcon = QIcon("icon.png")
        self.setWindowIcon(appIcon)

    # to center the application window at the beginning
    def center(self):
        qRect = self.frameGeometry()
        centerPoint = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qRect.moveCenter(centerPoint)
        self.move(qRect.topLeft())

    def mousePressEvent(self, event:QMouseEvent):
        print(event.x(),event.y())
        self.colorDefaultLabels()

# run the application and show the window
app = QApplication(sys.argv)
window = Window()
window.show()

app.exec_()
sys.exit(0)