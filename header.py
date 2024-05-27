from PyQt5.QtWidgets import QLabel

class Header(QLabel):
    def __init__(self):
        super().__init__('Header')
        self.setFixedHeight(80)  # Set header height to 80 pixels
        self.setStyleSheet("border-bottom: 2px solid #87DDE0; padding: 10px;")
