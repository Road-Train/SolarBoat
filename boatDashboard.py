from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

class BoatDashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the main layout for the boat dashboard
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(10, 10, 10, 10)  # Set margins to 10px
        main_layout.setSpacing(0)  # Set spacing to zero

        # Single big box for boat dashboard
        dashboard = QLabel('Boat Dashboard')
        dashboard.setStyleSheet("background-color: lightblue; padding: 10px; border: 2px solid #F7A072;")
        main_layout.addWidget(dashboard)

        self.setLayout(main_layout)
