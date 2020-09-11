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
        self.setVoltageLabels()
        self.setCurrentLabels()

    # add all transistors label at the start above the schematic
    def setTransistorsLabels(self):
        # set default font for all transistors label
        font = QFont("SansSerif",14,italic=True)

        # set all transistors label
        self.trans1a = QLabel(self.label)
        self.trans1a.setText("M1a")
        self.trans1a.move(282,243)
        self.trans1a.setFont(font)

        self.trans2a = QLabel(self.label)
        self.trans2a.setText("M2a")
        self.trans2a.move(77,368)
        self.trans2a.setFont(font)

        self.trans3a = QLabel(self.label)
        self.trans3a.setText("M3a")
        self.trans3a.move(77,288)
        self.trans3a.setFont(font)

        self.trans4a = QLabel(self.label)
        self.trans4a.setText("M4a")
        self.trans4a.move(77,178)
        self.trans4a.setFont(font)

        self.trans5a = QLabel(self.label)
        self.trans5a.setText("M5a")
        self.trans5a.move(77,110)
        self.trans5a.setFont(font)

        self.trans1b = QLabel(self.label)
        self.trans1b.setText("M1b")
        self.trans1b.move(337, 243)
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

        self.trans6 = QLabel(self.label)
        self.trans6.setText("M6")
        self.trans6.move(337, 150)
        self.trans6.setFont(font)

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

        self.trans6.setStyleSheet("color: blue")

    def setVoltageLabels(self):
        # set default fonts for all components label
        font1 = QFont("SansSerif", 14, italic=True)
        font2 = QFont("SansSerif", 11, italic=True)

        label1 = QLabel(self.label)
        label1.setText("V")
        label1.move(182, 290)
        label1.setFont(font1)
        label1.setStyleSheet("color: blue")

        label2 = QLabel(self.label)
        label2.setText("cascn")
        label2.move(195, 297)
        label2.setFont(font2)
        label2.setStyleSheet("color: blue")

        label3 = QLabel(self.label)
        label3.setText("V")
        label3.move(182, 245)
        label3.setFont(font1)
        label3.setStyleSheet("color: blue")

        label4 = QLabel(self.label)
        label4.setText("in+")
        label4.move(195, 253)
        label4.setFont(font2)
        label4.setStyleSheet("color: blue")

        label5 = QLabel(self.label)
        label5.setText("V")
        label5.move(35, 232)
        label5.setFont(font1)
        label5.setStyleSheet("color: blue")

        label6 = QLabel(self.label)
        label6.setText("out-")
        label6.move(48, 240)
        label6.setFont(font2)
        label6.setStyleSheet("color: blue")

        label7 = QLabel(self.label)
        label7.setText("V")
        label7.move(182, 175)
        label7.setFont(font1)
        label7.setStyleSheet("color: blue")

        label8 = QLabel(self.label)
        label8.setText("cascp")
        label8.move(195, 183)
        label8.setFont(font2)
        label8.setStyleSheet("color: blue")

        label9 = QLabel(self.label)
        label9.setText("V")
        label9.move(220, 150)
        label9.setFont(font1)
        label9.setStyleSheet("color: blue")

        label10 = QLabel(self.label)
        label10.setText("cmfp")
        label10.move(233, 158)
        label10.setFont(font2)
        label10.setStyleSheet("color: blue")

        label11 = QLabel(self.label)
        label11.setText("V")
        label11.move(215, 90)
        label11.setFont(font1)
        label11.setStyleSheet("color: blue")

        label12 = QLabel(self.label)
        label12.setText("biasp")
        label12.move(228, 98)
        label12.setFont(font2)
        label12.setStyleSheet("color: blue")

        label13 = QLabel(self.label)
        label13.setText("V")
        label13.move(420, 290)
        label13.setFont(font1)
        label13.setStyleSheet("color: blue")

        label14 = QLabel(self.label)
        label14.setText("cascn")
        label14.move(433, 297)
        label14.setFont(font2)
        label14.setStyleSheet("color: blue")

        label15 = QLabel(self.label)
        label15.setText("V")
        label15.move(441, 245)
        label15.setFont(font1)
        label15.setStyleSheet("color: blue")

        label16 = QLabel(self.label)
        label16.setText("in-")
        label16.move(454, 253)
        label16.setFont(font2)
        label16.setStyleSheet("color: blue")

        label17 = QLabel(self.label)
        label17.setText("V")
        label17.move(420, 175)
        label17.setFont(font1)
        label17.setStyleSheet("color: blue")

        label18 = QLabel(self.label)
        label18.setText("cascp")
        label18.move(433, 183)
        label18.setFont(font2)
        label18.setStyleSheet("color: blue")

        label19 = QLabel(self.label)
        label19.setText("V")
        label19.move(577, 232)
        label19.setFont(font1)
        label19.setStyleSheet("color: blue")

        label20 = QLabel(self.label)
        label20.setText("out+")
        label20.move(590, 240)
        label20.setFont(font2)
        label20.setStyleSheet("color: blue")

        label21 = QLabel(self.label)
        label21.setText("V")
        label21.move(310, 320)
        label21.setFont(font1)
        label21.setStyleSheet("color: blue")

        label22 = QLabel(self.label)
        label22.setText("biasn")
        label22.move(323, 327)
        label22.setFont(font2)
        label22.setStyleSheet("color: blue")

        label23 = QLabel(self.label)
        label23.setText("V")
        label23.move(310, 37)
        label23.setFont(font1)
        label23.setStyleSheet("color: blue")

        label24 = QLabel(self.label)
        label24.setText("DD")
        label24.move(323, 45)
        label24.setFont(font2)
        label24.setStyleSheet("color: blue")

    def setCurrentLabels(self):
        # set default fonts for all components label
        font1 = QFont("SansSerif", 11, italic=True)
        font2 = QFont("SansSerif", 9, italic=True)

        label1 = QLabel(self.label)
        label1.setText("I")
        label1.move(235, 207)
        label1.setFont(font1)
        label1.setStyleSheet("color: blue")

        label2 = QLabel(self.label)
        label2.setText("bias")
        label2.move(240, 215)
        label2.setFont(font2)
        label2.setStyleSheet("color: blue")

        label3 = QLabel(self.label)
        label3.setText("I")
        label3.move(392, 207)
        label3.setFont(font1)
        label3.setStyleSheet("color: blue")

        label4 = QLabel(self.label)
        label4.setText("bias")
        label4.move(397, 215)
        label4.setFont(font2)
        label4.setStyleSheet("color: blue")

        label5 = QLabel(self.label)
        label5.setText("I")
        label5.move(77, 77)
        label5.setFont(font1)
        label5.setStyleSheet("color: blue")

        label6 = QLabel(self.label)
        label6.setText("bias")
        label6.move(82, 85)
        label6.setFont(font2)
        label6.setStyleSheet("color: blue")

        label7 = QLabel(self.label)
        label7.setText("2I")
        label7.move(340, 77)
        label7.setFont(font1)
        label7.setStyleSheet("color: blue")

        label8 = QLabel(self.label)
        label8.setText("bias")
        label8.move(355, 85)
        label8.setFont(font2)
        label8.setStyleSheet("color: blue")

        label9 = QLabel(self.label)
        label9.setText("I")
        label9.move(552, 77)
        label9.setFont(font1)
        label9.setStyleSheet("color: blue")

        label10 = QLabel(self.label)
        label10.setText("bias")
        label10.move(557, 85)
        label10.setFont(font2)
        label10.setStyleSheet("color: blue")

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
        self.colorDefaultLabels()
        self.redClickedTransistor(event.x(),event.y())

    # red the transistor if the mouse position within its range
    def redClickedTransistor(self,x,y):
        x1_a1 = 230
        y1_a1 = 280
        x2_a1 = 290
        y2_a1 = 230

        x1_b1 = 365
        y1_b1 = 280
        x2_b1 = 425
        y2_b1 = 230

        x1_a2 = 100
        y1_a2 = 400
        x2_a2 = 170
        y2_a2 = 350

        x1_b2 = 490
        y1_b2 = 400
        x2_b2 = 555
        y2_b2 = 350

        x1_a3 = 100
        y1_a3 = 320
        x2_a3 = 170
        y2_a3 = 265

        x1_b3 = 490
        y1_b3 = 320
        x2_b3 = 555
        y2_b3 = 265

        x1_a4 = 100
        y1_a4 = 210
        x2_a4 = 170
        y2_a4 = 160

        x1_b4 = 490
        y1_b4 = 210
        x2_b4 = 555
        y2_b4 = 160

        x1_a5 = 100
        y1_a5 = 145
        x2_a5 = 170
        y2_a5 = 95

        x1_b5 = 490
        y1_b5 = 145
        x2_b5 = 555
        y2_b5 = 95

        x1_6 = 280
        y1_6 = 180
        x2_6 = 345
        y2_6 = 140

        if self.withinRange(x,y,x1_a1,y1_a1,x2_a1,y2_a1) or self.withinRange(x,y,x1_b1,y1_b1,x2_b1,y2_b1):
            self.trans1a.setStyleSheet("color: red")
            self.trans1b.setStyleSheet("color: red")
        elif self.withinRange(x,y,x1_a2,y1_a2,x2_a2,y2_a2) or self.withinRange(x,y,x1_b2,y1_b2,x2_b2,y2_b2):
            self.trans2a.setStyleSheet("color: red")
            self.trans2b.setStyleSheet("color: red")
        elif self.withinRange(x,y,x1_a3,y1_a3,x2_a3,y2_a3) or self.withinRange(x,y,x1_b3,y1_b3,x2_b3,y2_b3):
            self.trans3a.setStyleSheet("color: red")
            self.trans3b.setStyleSheet("color: red")
        elif self.withinRange(x,y,x1_a4,y1_a4,x2_a4,y2_a4) or self.withinRange(x,y,x1_b4,y1_b4,x2_b4,y2_b4):
            self.trans4a.setStyleSheet("color: red")
            self.trans4b.setStyleSheet("color: red")
        elif self.withinRange(x,y,x1_a5,y1_a5,x2_a5,y2_a5) or self.withinRange(x,y,x1_b5,y1_b5,x2_b5,y2_b5):
            self.trans5a.setStyleSheet("color: red")
            self.trans5b.setStyleSheet("color: red")
        elif self.withinRange(x,y,x1_6,y1_6,x2_6,y2_6):
            self.trans6.setStyleSheet("color: red")

    def withinRange(self,x,y,x1,y1,x2,y2):
        if x >= x1 and x <= x2 and y <= y1 and y >= y2:
            return True
        else:
            return False

# run the application and show the window
app = QApplication(sys.argv)
window = Window()
window.show()

app.exec_()
sys.exit(0)