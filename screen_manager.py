from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

from screens import code_screen, decode_screen, start_screen, about_screen


class Screen(QWidget):
    def __init__(self, class_name):
        super().__init__()
        self.ui = class_name
        self.ui.setupUi(self)