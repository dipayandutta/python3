import sys
from PyQt5.QtWidgets import QWidget,QDesktopWidget,QApplication,QMessageBox,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300,400,300,200)
        self.setWindowTitle('File Menu Application')
        self.centre()
        self.menuApplication()

        self.show()


    def centre(self):

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message','Quit?',QMessageBox.Yes|QMessageBox.No , QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def menuApplication(self):
        exitAct = QAction(QIcon('icon/gun.png'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit From Application')
        exitAct.triggered.connect(qApp.quit)

        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)


if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = Example()
    sys.exit(application.exec_())

        
            
