import sys
from PyQt5.QtWidgets import QWidget,QToolTip,QPushButton,QApplication
from PyQt5.QtGui import QFont

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('This is a <b>Widget Application</b>')

        btn = QPushButton('Click',self)
        btn.setToolTip('This is a <b>QPushButton</b>')
        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.show()


if __name__ == '__main__':

	application = QApplication(sys.argv)
	example = Example()
	sys.exit(application.exec_())