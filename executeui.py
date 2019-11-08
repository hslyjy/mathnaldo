from PyQt5.QtWidgets import *

class ExecuteUI(QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.btnOk = QPushButton("Play")
        self.btnSave = QPushButton("Save")
        self.btnLoad = QPushButton("Load")
        layout = QHBoxLayout()
        layout.addWidget(self.btnOk)
        layout.addWidget(self.btnSave)
        layout.addWidget(self.btnLoad)
        self.setLayout(layout)

