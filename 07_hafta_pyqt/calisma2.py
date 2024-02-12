import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

x = QWidget()

# x.show()

window1 = QPushButton("Tıkla")
window1.setWindowTitle('Deneme')
window1.resize(200, 50)
window1.show()

aa = QLabel("Merhaba")
aa.setWindowTitle('Label')
aa.resize(500, 500)
aa.show()

app.exec()
