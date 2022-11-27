import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(200, 100, 1280, 720)
        self.setWindowTitle("Browser application")
        self.setStyleSheet("background-color : rgb(250,250,250)")
        self.initUI()
        
    def initUI(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))
        self.setCentralWidget(self.browser)
        
        self.nav = QToolBar("Navigation")
        self.nav.setIconSize(QSize(16,16))
        self.addToolBar(self.nav)


        #Back btn
        self.back_btn = QAction(QIcon(os.path.join("Icons","back.png")), "Back",self)
        self.back_btn.setStatusTip("Go back to previous page")  
        self.back_btn.triggered.connect(self.browser.back)
        self.nav.addAction(self.back_btn)

        self.forward_btn = QAction(QIcon(os.path.join("Icons","forward.png")),"Forward",self)
        self.forward_btn.setStatusTip("Go forward to next page")
        self.forward_btn.triggered.connect(self.browser.forward)
        self.nav.addAction(self.forward_btn)

        self.reload_btn = QAction(QIcon(os.path.join("Icons","refresh.png")), "Reload",self)
        self.reload_btn.setStatusTip("Reload page")
        self.reload_btn.triggered.connect(self.browser.reload)
        self.nav.addAction(self.reload_btn)

        self.go_home_btn = QAction(QIcon(os.path.join("Icons","home-page.png")),"Home",self)
        self.go_home_btn.setStatusTip("Go to Home ")
        self.go_home_btn.triggered.connect(self.go_home)
        self.nav.addAction(self.go_home_btn)

    def go_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))
        

        


def main():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()