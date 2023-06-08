from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        navbar = QToolBar()
        self.addToolBar(navbar)
        back_Button = QAction('Back', self)
        back_Button.triggered.connect(self.browser.back)
        navbar.addAction(back_Button)

        front_Button = QAction('Forwad', self)
        front_Button.triggered.connect(self.browser.forward)
        navbar.addAction(front_Button)

        
        Reload_Button = QAction('Reload', self)
        Reload_Button.triggered.connect(self.browser.reload)
        navbar.addAction(Reload_Button)

        home_bth = QAction('Home',self)
        home_bth.triggered.connect(self.navigate_home)
        navbar.addAction(home_bth)

        self.urL_bar = QLineEdit()
        self.urL_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.urL_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        url = QUrl('http://google.com')
        self.browser.setUrl(url)  

    def navigate_to_url(self):
        url = self.urL_bar.text()
        self.browser.setUrl(url)   

    def update_url(self, q):
        self.urL_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName('GLASS BROWSER')
window = MainWindow()
app.exec_()