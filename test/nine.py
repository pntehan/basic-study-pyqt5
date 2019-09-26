import sys
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication, QPushButton, QFrame, QSlider, QLabel, QProgressBar, QCalendarWidget
from PyQt5.QtCore import Qt, QBasicTimer

class Example(QWidget):
    """docstring for Example"""
    def __init__(self):
        super(Example, self).__init__()
        self.initUI5()

    def initUI(self):
        cb = QCheckBox("Show title", self)
        cb.move(20, 20)
        # default be checked
        # cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setGeometry(300, 300, 350, 300)
        # self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle("Not Simple")
        else:
            self.setWindowTitle("Simple")

    def initUI2(self):
        from PyQt5.QtGui import QColor
        self.col = QColor(0, 0, 0)
        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget { background-color: %s }"%self.col.name())

        redb = QPushButton("Red", self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.setColor)

        greenb = QPushButton("Green", self)
        greenb.setCheckable(True)
        greenb.move(10, 60)
        greenb.clicked[bool].connect(self.setColor)

        blueb = QPushButton("Blue", self)
        blueb.setCheckable(True)
        blueb.move(10, 110)
        blueb.clicked[bool].connect(self.setColor)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def setColor(self, pressed):
        source = self.sender()
        val = 255 if pressed else 0
        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)
        self.square.setStyleSheet("QFrame { background-color: %s }"%self.col.name())

    def initUI3(self):
        from PyQt5.QtGui import QPixmap, QIcon

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)

        self.label = QLabel(self)
        self.label.setPixmap(QPixmap("../1.ico"))
        self.label.setGeometry(160, 40, 80, 30)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowIcon(QIcon("../title.png"))
        self.setWindowTitle("Simple")
        self.show()

    def changeValue(self, value):
        from PyQt5.QtGui import QPixmap
        if value == 0:
            self.label.setPixmap(QPixmap("../1.ico"))
        elif value > 0 and value <= 30:
            self.label.setPixmap(QPixmap("../2.ico"))
        elif value > 30 and value <= 80:
            self.label.setPixmap(QPixmap("../3.ico"))
        else:
            self.label.setPixmap(QPixmap("../4.ico"))

    def initUI4(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton("Start", self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText("Start")
        else:
            self.timer.start(100, self)
            self.btn.setText("Stop")

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText("Finished")
            # self.btn.clicked.connect(self.doAction)
            return
        self.step += 10
        self.pbar.setValue(self.step)

    def initUI5(self):
        from PyQt5.QtCore import QDate
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lal = QLabel(self)
        date = cal.selectedDate()
        self.lal.setText(date.toString())
        self.lal.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def showDate(self, date):
        self.lal.setText(date.toString())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


























