import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
 
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI2()
        
        
    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)
 
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
        
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')    
        self.show()

    def initUI2(self):
        from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
 
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
 
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        
        self.setLayout(vbox)    
        
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())