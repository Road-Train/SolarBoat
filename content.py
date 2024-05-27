from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSpacerItem, QSizePolicy

class Content(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create the main layout for the content
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        main_layout.setSpacing(0)  # Set spacing to zero

        # Single big box on top
        big_box = QLabel('Main Content')
        big_box.setFixedSize(1280, 640)
        big_box.setStyleSheet("background-color: lightgrey; padding: 10px; border-bottom: 2px solid #F7A072;")
        main_layout.addWidget(big_box)

        # Create a horizontal layout for the two smaller parts at the bottom
        bottom_layout = QHBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)  # Set margins to zero
        bottom_layout.setSpacing(0)  # Set spacing to zero

        # First smaller part
        small_box1 = QLabel('Small Content 1')
        small_box1.setFixedSize(640, 320)
        small_box1.setStyleSheet("background-color: lightblue; padding: 10px; border-top: 2px solid #F7A072;")
        small_box1.setContentsMargins(0,0,0,0)
        bottom_layout.addWidget(small_box1)

        # Second smaller part
        small_box2 = QLabel('Small Content 2')
        small_box2.setFixedSize(640, 320)
        small_box2.setStyleSheet("background-color: lightgreen; padding: 10px; border-top: 2px solid #F7A072;")
        bottom_layout.addWidget(small_box2)

        # Add spacer item to align the right side of bottom right box with big box
        spacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
        bottom_layout.addItem(spacer)

        # Add the bottom layout to the main layout
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)
