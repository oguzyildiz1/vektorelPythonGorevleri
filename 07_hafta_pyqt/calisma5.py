import sys
from PyQt6.QtWidgets import *

app = QApplication(sys.argv)

window = QMainWindow()

layout = QVBoxLayout()

layout.addWidget(QComboBox())
layout.addWidget(QDateEdit())
layout.addWidget(QDateTimeEdit())
layout.addWidget(QDial())
layout.addWidget(QComboBox())
layout.addWidget(QFontComboBox())
layout.addWidget(QSlider())



widget = QWidget()
widget.setLayout(layout)

window.setCentralWidget(widget)

window.show()

app.exec()