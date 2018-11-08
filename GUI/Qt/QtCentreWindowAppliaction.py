import sys
from PyQt5.QtWidgets import QWidget, QDesktopWidget , QApplication ,QMessageBox


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.resize(250,140)
        self.centre()

        self.setWindowTitle('Center Window Application')
        self.show()

    def centre(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):

        reply = QMessageBox.question(self,'Message','Quit ?',QMessageBox.Yes|QMessageBox.No ,QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':

    application = QApplication(sys.argv)
    example = Example()
    sys.exit(application.exec_())
