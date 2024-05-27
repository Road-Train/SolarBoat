from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class BoatInfo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the main layout for the content
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        main_layout.setSpacing(0)  # Set spacing to zero

        # Single big box
        big_box = QLabel('Main Content')
        big_box.setFixedSize(1280, 960)  # Adjusted size to 1280x960
        big_box.setStyleSheet("background-color: lightgrey; padding: 10px; border-bottom: 2px solid #F7A072;")
        main_layout.addWidget(big_box)

        self.setLayout(main_layout)
