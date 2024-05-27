import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt, QSize

class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PyQt5 Layout Example')
        self.setFixedSize(1920, 1080)  # Set fixed window size
        self.showFullScreen()  # Enable fullscreen

        # Create the main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set layout margins to zero

        # Header
        header = QLabel('Header', self)
        header.setFixedHeight(80)  # Set header height to 80 pixels
        header.setStyleSheet("background-color: lightblue; padding: 10px;")
        main_layout.addWidget(header)

        # Create a horizontal layout for the menu and main application area
        menu_and_app_layout = QHBoxLayout()

        # Create the sidebar menu
        menu_section = QWidget()
        menu_section_layout = QVBoxLayout(menu_section)
        menu_section.setMaximumWidth(477)  # Set the width of the menu section
        menu_section.setContentsMargins(104, 52, 0, 0)  # Set top and left margin

        # Menu Header
        menu_header = QLabel('Menu', self)
        menu_header.setFixedHeight(52)
        menu_header.setStyleSheet("background-color: lightblue; padding: 10px;")
        menu_section_layout.addWidget(menu_header)

        # Create scroll area for the menu
        menu_scroll = QScrollArea()
        menu_scroll.setWidgetResizable(True)

        menu_content = QWidget()
        menu_content_layout = QVBoxLayout(menu_content)
        menu_content_layout.setAlignment(Qt.AlignTop)

        # Add menu items to the menu
        for i in range(1, 20):  # Adjust this range as needed to fill the menu
            menu_item = QLabel(f'Menu Item {i}', self)
            menu_item.setFixedHeight(96)
            menu_item.setStyleSheet("background-color: lightgrey; padding: 10px; margin-bottom: 3px;")
            menu_content_layout.addWidget(menu_item)

        menu_scroll.setWidget(menu_content)
        menu_scroll.setFixedHeight(452)  # Set the height of the scroll area

        menu_section_layout.addWidget(menu_scroll)

        # Add the menu section to the horizontal layout
        menu_and_app_layout.addWidget(menu_section)

        # Create the main application area
        app_section = QWidget()
        app_section_layout = QVBoxLayout(app_section)

        # Box 1
        box1 = QLabel('Box 1', self)
        box1.setFixedSize(1088, 416)
        box1.setStyleSheet("background-color: lightgreen; padding: 10px;")
        app_section_layout.addWidget(box1)

        # Create a horizontal layout for Box 2 and Box 3
        box23_layout = QHBoxLayout()

        # Box 2
        box2 = QLabel('Box 2', self)
        box2.setFixedSize(724, 267)
        box2.setStyleSheet("background-color: lightcoral; padding: 10px; margin-top: 3px;")
        box23_layout.addWidget(box2)

        # Box 3
        box3 = QLabel('Box 3', self)
        box3.setFixedSize(364, 267)
        box3.setStyleSheet("background-color: lightblue; padding: 10px; margin-top: 3px;")
        box23_layout.addWidget(box3)

        # Add Box 2 and Box 3 layout to the main application area layout
        app_section_layout.addLayout(box23_layout)

        # Add the app section to the horizontal layout
        menu_and_app_layout.addWidget(app_section)

        # Add the horizontal layout to the main layout
        main_layout.addLayout(menu_and_app_layout)

        # Footer
        footer = QLabel('Footer', self)
        footer.setFixedHeight(80)  # Set footer height to 80 pixels
        footer.setStyleSheet("background-color: lightblue; padding: 10px;")
        main_layout.addWidget(footer)

        # Set the main widget as the central widget
        self.setCentralWidget(main_widget)

def main():
    app = QApplication(sys.argv)
    ex = Application()
    ex.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
