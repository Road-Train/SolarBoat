from PyQt5.QtWidgets import QVBoxLayout, QLabel, QScrollArea, QWidget
from PyQt5.QtCore import Qt

class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create layout for menu
        layout = QVBoxLayout(self)
        layout.setContentsMargins(100, 0, 50, 0)  # Set margins (left, top, right, bottom)
        layout.setSpacing(0)  # Set spacing between items

        # Set the width of the entire menu section to 448 px
        self.setFixedWidth(512)

        # Apply border style
        self.setStyleSheet("border: 1px solid #F7A072;")

        # Menu Header
        menu_header = QLabel('Menu')
        menu_header.setFixedHeight(52)
        menu_header.setStyleSheet("background-color: lightblue; padding: 10px;")
        layout.addWidget(menu_header)

        # Create scroll area for the menu
        menu_scroll = QScrollArea()
        menu_scroll.setWidgetResizable(True)

        menu_content = QWidget()
        menu_content_layout = QVBoxLayout(menu_content)
        menu_content_layout.setAlignment(Qt.AlignTop)

        # Add menu items to the menu
        for i in range(1, 20):  # Adjust this range as needed to fill the menu
            menu_item = QLabel(f'Menu Item {i}')
            menu_item.setFixedHeight(96)
            menu_item.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
            menu_content_layout.addWidget(menu_item)

        menu_scroll.setWidget(menu_content)
        menu_scroll.setFixedHeight(452)  # Set the height of the scroll area

        layout.addWidget(menu_scroll)
