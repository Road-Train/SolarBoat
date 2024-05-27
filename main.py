import sys
from PyQt5.QtGui import QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from header import Header
from footer import Footer
from menu import Menu
from body import Body  # Assuming Body is the class representing the initial content
from boatInfo import BoatInfo


class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Solar Boat Application')
        self.setFixedSize(1920, 1080)  # Set fixed window size
        self.showFullScreen()  # Enable fullscreen

        # Register the font file
        font_id = QFontDatabase.addApplicationFont('src/fonts/ocr-a-extended.ttf')
        # Get the font family name
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        # Create the font object
        custom_font = QFont(font_family)
        custom_font.setPixelSize(16)
        custom_font.setBold(True)

        # Set the default font for the application
        QApplication.instance().setFont(custom_font)

        self.setStyleSheet("background-image: url(src/img/BackgroundUI.png);")
        # self.setStyleSheet('background-color: rgb(255, 255, 255);')

        # Create the main widget and layout
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Set layout margins to zero

        # Header
        header = Header()
        header.setFont(custom_font)  # Set font for header
        main_layout.addWidget(header)

        # Create a horizontal layout for the menu and main application area
        menu_and_app_layout = QHBoxLayout()

        # Create the sidebar menu
        menu = Menu()
        menu.setFont(custom_font)  # Set font for menu
        menu_and_app_layout.addWidget(menu)

        # Create the initial content area (Body)
        initial_content = Body()  # Assuming Body represents the initial content
        initial_content.setFont(custom_font)  # Set font for content
        menu_and_app_layout.addWidget(initial_content)

        # Add the horizontal layout to the main layout
        main_layout.addLayout(menu_and_app_layout)

        # Footer
        footer = Footer()
        footer.setFont(custom_font)  # Set font for footer
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


