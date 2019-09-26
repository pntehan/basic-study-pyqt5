import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
from PyQt5.QtGui import QIcon
 
class Example(QMainWindow):
    """stateBar"""
    def __init__(self):
        super().__init__()
        self.initUI3()
        
        
    def initUI(self):               
        self.statusBar().showMessage('Ready')
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Simple')    
        self.show()

    def initUI2(self):
        exitAction = QAction(QIcon("../title.png"), "&Exit", self)
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit Application")
        exitAction.triggered.connect(QApplication.quit)

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(exitAction)
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

    def initUI3(self):
        """I don't like this method."""
        from PyQt5.QtWidgets import QTextEdit
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)
 
        exitAction = QAction(QIcon("../title.png"), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.close)
 
        self.statusBar()
 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
 
        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exitAction)
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle("Simple")
        self.setWindowIcon(QIcon("../title.png"))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())