import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon, QFont, QCloseEvent

class Example(QWidget):
    """docstring for Example"""
    def __init__(self):
        super(Example, self).__init__()
        # self.initUI()
        self.initQuitUI()

    def initUI(self):
        # This static function is aim to chose the type of font. In this case, we use 10px smooth font.
        QToolTip.setFont(QFont("SansSerif", 10))
        # Create a tip, we call it settooltip, we can use kinds of types of text.
        self.setToolTip("This is a <b>QWidget</b> widget")
        # create a pushbutton and set a tooltip for this button.
        btn = QPushButton("Button", self)
        btn.setToolTip("This is a <b>QPushButton</b> widget")
        # Button's size be setted default setting.
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def initQuitUI(self):
        """set a button be called quit, and it's aim to close window by click"""
        from PyQt5.QtCore import QCoreApplication
        qbtn = QPushButton("Quit", self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.move(50, 50)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Message",
            "Are you sure to quit?", QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())