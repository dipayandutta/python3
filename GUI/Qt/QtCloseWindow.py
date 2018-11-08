import sys
from PyQt5.QtWidgets import QWidget , QPushButton , QApplication 

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Quit Application')
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = Example()
    sys.exit(application.exec_())
