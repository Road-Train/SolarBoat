from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class Content(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the layout for the content
        layout = QVBoxLayout(self)

        # Single big box
        big_box = QLabel('Main Content')
        big_box.setFixedSize(1280, 640)
        big_box.setStyleSheet("background-color: lightgrey; padding: 10px;")
        layout.addWidget(big_box)
