from PyQt6 import QtWidgets

from screen_manager import Screen
from screens import about_screen, code_screen, decode_screen, start_screen
from screens.main_app import Ui_MainWindow

import algorithms


class App(QtWidgets.QMainWindow):
    """
    The main class of app
    """
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.screen_loader()
        self.button_loader()

    
    def button_loader(self):
        """
        Connecting buttons to functions
        """
        self.start_screen.ui.menu.buttonClicked.connect(self.menu_click)

        back = lambda: self.ui.stackedWidget.setCurrentIndex(0)
        self.code_screen.ui.back_button.clicked.connect(back)
        self.decode_screen.ui.back_button.clicked.connect(back)
        self.about_screen.ui.back_button.clicked.connect(back)

        self.code_screen.ui.run_button.clicked.connect(self.code)
        self.decode_screen.ui.run_button.clicked.connect(self.decode)


    def screen_loader(self):
        """
        Loading all screens for app
        """
        self.start_screen = Screen(start_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.start_screen)

        self.code_screen = Screen(code_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.code_screen)
        
        self.decode_screen = Screen(decode_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.decode_screen)
        
        self.about_screen = Screen(about_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.about_screen)


    def menu_click(self, pressed_button):
        """
        Checking press button in start menu
        """
        for i, button in enumerate(self.start_screen.ui.menu.buttons()):
            if button == pressed_button:
                self.ui.stackedWidget.setCurrentIndex(i + 1)
                break


    def code(self):
        text = self.code_screen.ui.input.text()
        code = algorithms.Code(text)
        self.code_screen.ui.output.setText(code.result)


    def decode(self):
        text = self.decode_screen.ui.input.text()
        code = algorithms.Decode(text)
        self.decode_screen.ui.output.setText(code + 'расшифровал')
