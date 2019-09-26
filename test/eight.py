import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QInputDialog, QApplication, QMainWindow

class Example(QWidget):
    """docstring for Example"""
    def __init__(self):
        super(Example, self).__init__()
        self.initUI2()

    def initUI(self):
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(130, 22)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, "Input Dialog", "Enter your name:")
        if ok:
            self.le.setText(str(text))

    def initUI2(self):
        from PyQt5.QtGui import QColor
        col = QColor(0, 0, 0)
        self.btn = QPushButton("Dialog", self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showColor)
        from PyQt5.QtWidgets import QFrame
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color:%s }"%col.name())
        self.frm.setGeometry(130, 22, 100, 100)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def showColor(self):
        from PyQt5.QtWidgets import QColorDialog
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color:%s }"%col.name())

    def initUI3(self):
        from PyQt5.QtWidgets import QVBoxLayout, QSizePolicy, QLabel
        vbox = QVBoxLayout()
        btn = QPushButton("font", self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        vbox.addWidget(btn)
        btn.clicked.connect(self.showFont)

        self.lab = QLabel("Knowledge only matters", self)
        self.lab.move(130, 20)

        vbox.addWidget(self.lab)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        from PyQt5.QtGui import QIcon
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def showFont(self):
        from PyQt5.QtWidgets import QFontDialog
        font, ok = QFontDialog.getFont()
        if ok:
            self.lab.setFont(font)

class Example2(QMainWindow):
    """docstring for Example2"""
    def __init__(self):
        super(Example2, self).__init__()
        self.initUI()
    
    def initUI(self):
        from PyQt5.QtWidgets import QTextEdit, QAction
        from PyQt5.QtGui import QIcon
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        self.statusBar()
        openfile = QAction(QIcon("../title.png"), "open", self)
        openfile.setShortcut("Ctrl+O")
        openfile.setStatusTip("Open new File")
        openfile.triggered.connect(self.showFile)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(openfile)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def showFile(self):
        from PyQt5.QtWidgets import QFileDialog
        frame = QFileDialog.getOpenFileName(self, "Open file")
        if frame[0]:
            with open(frame[0], "r") as fp:
                data = fp.read()
                self.textEdit.setText(data)

        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Example2()
    sys.exit(app.exec_())

