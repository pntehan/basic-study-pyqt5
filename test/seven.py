import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication

class Communicate(QObject):
    """docstring for Communicate"""
    closeApp = pyqtSignal()

class Example(QMainWindow):
    """docstring for Example"""
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
