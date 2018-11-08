import sys
from PyQt5.QtWidgets import QWidget , QMessageBox,QApplication,QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('MessageBox Application')
        self.quitButton()
        self.show()

        
    def closeEvent(self,event):

        reply = QMessageBox.question(self,'Message','Are you want to quit',QMessageBox.Yes|QMessageBox.No , QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()

        else:
            event.ignore()

    def quitButton(self):

        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

if __name__ == '__main__':

    application = QApplication(sys.argv)
    example = Example()
    sys.exit(application.exec_())

