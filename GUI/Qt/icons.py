import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Icon Application')
        self.setWindowIcon(QIcon('icons/mask.png'))

        self.show()


def main():
    application = QApplication(sys.argv)
    example = Example()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
