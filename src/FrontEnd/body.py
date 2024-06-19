from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class Body(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the layout for the body
        layout = QVBoxLayout(self)

        # Box 1
        box1 = QLabel('Box 1')
        box1.setFixedSize(1088, 416)
        layout.addWidget(box1)

        # Box 2
        box2 = QLabel('Box 2')
        box2.setFixedSize(724, 267)
        layout.addWidget(box2)

        # Box 3
        box3 = QLabel('Box 3')
        box3.setFixedSize(364, 267)
        layout.addWidget(box3)
