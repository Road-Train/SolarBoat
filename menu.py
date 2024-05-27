from PyQt5.QtWidgets import QVBoxLayout, QPushButton, QScrollArea, QWidget, QMessageBox, QHBoxLayout
from PyQt5.QtCore import Qt
from boatInfo import BoatInfo  # Import BoatInfo class

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
        self.setStyleSheet("border: 2px solid #F7A072;")

        # Menu Header
        menu_header = QPushButton('Menu')
        menu_header.setFixedHeight(52)
        menu_header.setStyleSheet("background-color: lightblue; padding: 10px;")
        layout.addWidget(menu_header)

        # Create scroll area for the menu
        menu_scroll = QScrollArea()
        menu_scroll.setWidgetResizable(True)

        menu_content = QWidget()
        menu_content_layout = QVBoxLayout(menu_content)
        menu_content_layout.setAlignment(Qt.AlignTop)

        # Add 7 menu items to the menu as buttons
        menu_button1 = QPushButton('Menu Item 1')
        menu_button1.setFixedHeight(96)
        menu_button1.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
        menu_button1.clicked.connect(self.openPopup)  # Connect button to openPopup function
        menu_content_layout.addWidget(menu_button1)

        menu_button2 = QPushButton('Menu Item 2')
        menu_button2.setFixedHeight(96)
        menu_button2.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
        menu_button2.clicked.connect(self.swapContent)  # Connect button to swapContent function
        menu_content_layout.addWidget(menu_button2)

        menu_button3 = QPushButton('Menu Item 3')
        menu_button3.setFixedHeight(96)
        menu_button3.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
        menu_content_layout.addWidget(menu_button3)

        menu_button4 = QPushButton('Menu Item 4')
        menu_button4.setFixedHeight(96)
        menu_button4.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
        menu_content_layout.addWidget(menu_button4)

        menu_button5 = QPushButton('Menu Item 5')
        menu_button5.setFixedHeight(96)
        menu_button5.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
        menu_content_layout.addWidget(menu_button5)

        menu_button6 = QPushButton('Menu Item 6')
        menu_button6.setFixedHeight(96)
        menu_button6.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
        menu_content_layout.addWidget(menu_button6)

        menu_button7 = QPushButton('Menu Item 7')
        menu_button7.setFixedHeight(96)
        menu_button7.setStyleSheet("background-color: lightgrey; padding: 0; margin: 0;")
        menu_content_layout.addWidget(menu_button7)

        menu_scroll.setWidget(menu_content)
        menu_scroll.setFixedHeight(452)  # Set the height of the scroll area

        layout.addWidget(menu_scroll)

    def openPopup(self):
        msg = QMessageBox()
        msg.setText("Hello World")
        msg.exec_()

    def swapContent(self):
        # Get the parent widget (Application)
        parent = self.parent().parent()  # Parent of Menu is QHBoxLayout, so getting its parent
        # Check if the parent widget has a content widget
        if hasattr(parent, "content"):
            # If it does, delete the content widget
            parent.content.deleteLater()
        # Toggle rendering between Body and Content
        if isinstance(parent.layout().itemAt(1).widget(), Body):
            # If currently showing Body, replace it with Content
            content = Content()
            content.setFont(self.font())
            parent.content = content
            parent.layout().replaceWidget(parent.layout().itemAt(1).widget(), content)
        else:
            # If currently showing Content, replace it with Body
            body = Body()
            body.setFont(self.font())
            parent.content = body
            parent.layout().replaceWidget(parent.layout().itemAt(1).widget(), body)
