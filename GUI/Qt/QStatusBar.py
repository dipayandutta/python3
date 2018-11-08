import sys
from PyQt5.QtWidgets import QWidget , QDesktopWidget , QApplication , QMessageBox,QMainWindow,QAction,qApp
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        exitAct = QAction(QIcon('icon/gun.png'),'&Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit From Application')
        exitAct.triggered.connect(qApp.quit)


        self.statusBar()

        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(exitAct)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Menu Application')
        self.show()

if __name__ == '__main__':
    application = QApplication(sys.argv)
    example = Example()
    sys.exit(application.exec_())
    
        
