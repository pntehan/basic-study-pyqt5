import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QApplication, QLineEdit, QFrame, QSplitter, QComboBox
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

class Example(QWidget):
    """docstring for Example"""
    def __init__(self):
        super(Example, self).__init__()
        self.initUI4()
    
    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("../small.png")

        lal = QLabel(self)
        lal.setPixmap(pixmap)

        hbox.addWidget(lal)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def initUI2(self):
        self.lal = QLabel(self)
        qle = QLineEdit(self)
        qle.move(60, 100)
        self.lal.move(60, 40)
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def onChanged(self, text):
        self.lal.setText(text)
        self.lal.adjustSize()

    def initUI3(self):
        hbox = QHBoxLayout(self)
        topleft = QFrame(self)
        topleft.setFrameShape(QFrame.StyledPanel)
        topright = QFrame(self)
        topright.setFrameShape(QFrame.StyledPanel)
        bottom = QFrame(self)
        bottom.setFrameShape(QFrame.StyledPanel)
        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def initUI4(self):
        self.lal = QLabel("Ubuntu", self)
        combo = QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Arch")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lal.move(50, 100)
        combo.activated[str].connect(self.onActivated)

        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def onActivated(self, text):
        self.lal.setText(text)
        self.lal.adjustSize()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

























