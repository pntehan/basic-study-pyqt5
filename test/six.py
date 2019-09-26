import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLCDNumber, QSlider, QVBoxLayout, QApplication, QMainWindow

class Example(QWidget):
    """docstring for Example"""
    def __init__(self):
        super(Example, self).__init__()
        self.initUI2()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def initUI2(self):
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_Up:
            print("Hello, World!")

class Example2(QMainWindow):
    """docstring for Example2"""
    def __init__(self):
        super(Example2, self).__init__()
        self.initUI()
    
    def initUI(self):
        from PyQt5.QtWidgets import QPushButton
        btn1 = QPushButton("Button 1", self)
        btn2 = QPushButton("Button 2", self)
        btn1.move(30, 50)
        btn2.move(150, 50)
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()
    
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text()+" was clicked")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())
