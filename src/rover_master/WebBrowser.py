import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import *
import base64
from io import BytesIO
from PIL import Image

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://keesiemeijer.github.io/maze-generator/#generate'))
        self.setCentralWidget(self.browser)

        self.line_edit = QLineEdit(self)
        self.line_edit.move(50, 50)

        button = QPushButton('Click me', self)
        button.setToolTip('This is a button')
        button.move(50, 100)
        button.clicked.connect(self.download_png)

        self.showMaximized()
    
    def download_png(self):
        user_input = self.line_edit.text()
        result = user_input.replace("data:image/png;base64,", "")
        print(result)
        decoded_data = base64.b64decode(result)

# Open the image from the decoded data
        img = Image.open(BytesIO(decoded_data))

# Save the image as PNG
        img.save("firstpandomm.png")  # output: "sdhfjhsdjfhsadh fjashdjfahsjdfhasjdhfjasd"

        

app = QApplication(sys.argv)
QApplication.setApplicationName('Maze Generator')
window = MainWindow()

app.exec()
