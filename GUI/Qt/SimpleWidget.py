import sys
from PyQt5.QtWidgets import QApplication , QWidget

def main():
    application = QApplication(sys.argv)

    W = QWidget()
    W.resize(250,150)
    W.move(300,300)
    W.setWindowTitle('Application')
    W.show()

    sys.exit(application.exec_())

if __name__ == '__main__':
    main()
