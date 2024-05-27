from PyQt5.QtWidgets import QLabel

class Footer(QLabel):
    def __init__(self):
        super().__init__('Footer')
        self.setFixedHeight(80)  # Set footer height to 80 pixels
        self.setStyleSheet("border-top: 2px solid #87DDE0; padding: 10px;")
