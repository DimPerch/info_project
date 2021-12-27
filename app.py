from random import choice

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QFontDatabase, QPixmap

import algorithms
from screen_manager import Screen
from screens import (about_screen, code_screen, decode_screen, game_screen,
                     main_app, start_screen)


class App(QtWidgets.QMainWindow):
    """
    The main class of app
    """
    def __init__(self):
        super(App, self).__init__()

        # load stylesheet
        file = QtCore.QFile(r"style.qss")
        file.open(QtCore.QIODeviceBase.OpenModeFlag.ReadOnly | QtCore.QIODeviceBase.OpenModeFlag.Text)
        stream = QtCore.QTextStream(file)
        self.setStyleSheet(stream.readAll())

        # load font
        font = QFontDatabase.addApplicationFont('resourses/font/Fairfax.ttf')
        if font == -1:
            print("ERROR: failed to connect font")

        self.game = Game(self)

        self.ui = main_app.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Шифратор / дешифратор XXX_FCTI")
        self.screen_loader()
        self.button_loader()

        self.size_timer = QtCore.QTimer(self)
        self.size_timer.timeout.connect(self.game.size_check)
        self.size_timer.start(100)

        self.img = [(QPixmap('resourses/img/00.jpg'), 'Англия, 1927 год\nВ городе свирепствует серийный убийца по кличке Хорни. В какой-то момент полиция поймала преступника, но Хорни успел оставить записку его подельнику. Полиция нашла эту записку, но она оказалось зашифрована. На допросе выяснили, что где-то в городе заложена бомба, и координаты зашифрованы. Команда Скотланд-Ярда бессильна. Вы - знаменитый на всю страну дешифровщик, и только вам удастся расшифровать координаты и спасти население от неминуемой гибели.'),
                    (QPixmap('resourses/img/01.jpg'), 'Сыщикам удалось перехватить шифр, но сколько они не пытались, расшифровать его не удалось. Вся надежда на тебя, великий детектив, раскрывший множество преступлений. Расшифруй шифр!'),
                    (QPixmap('resourses/img/02.jpg'), 'Тебе удалось расшифровать код, а сыщики благодаря этому смогли обезвредить бомбу. Спасибо тебе, ты спас множество жизней!'),
                    (QPixmap('resourses/img/03.jpg'), 'К сожалению, ты оказался не так хорош, твоя некомпетентность и купленная корочка, привели к смертям граждан...')]


    
    def button_loader(self):
        """
        Connecting buttons to functions
        """
        self.start_screen.ui.menu.buttonClicked.connect(self.menu_click)

        back = lambda: self.ui.stackedWidget.setCurrentIndex(0)
        self.code_screen.ui.back_button.clicked.connect(back)
        self.decode_screen.ui.back_button.clicked.connect(back)
        self.about_screen.ui.back_button.clicked.connect(back)
        self.game_screen.ui.back_button.clicked.connect(back)


        self.start_screen.ui.game_button.clicked.connect(self.start_game)
        self.code_screen.ui.run_button.clicked.connect(self.code)
        self.decode_screen.ui.run_button.clicked.connect(self.decode)

        self.game_screen.ui.next_button.clicked.connect(self.game.next_state)


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

        self.game_screen = Screen(game_screen.Ui_Form())
        self.ui.stackedWidget.addWidget(self.game_screen)


    def menu_click(self, pressed_button):
        """
        Checking press button in start menu
        """
        for i, button in enumerate(self.start_screen.ui.menu.buttons()):
            if button == pressed_button:
                self.ui.stackedWidget.setCurrentIndex(i + 1)
                break


    def code(self):
        """
        From text to code
        """
        text = self.code_screen.ui.input.text()
        code = algorithms.Code(text)
        self.code_screen.ui.output.setText(code.result)


    def decode(self):
        """
        From decode to text
        """
        text = self.decode_screen.ui.input.text()
        code = algorithms.Decode(text)
        self.decode_screen.ui.output.setText(code.result)


    def start_game(self):
        self.ui.stackedWidget.setCurrentIndex(4)   


class Game:
    def __init__(self, app):
        self.app = app
        self.state = 0
        """Dictionary with passwords"""
        self.words = ["Кирилл", "Дима", "Аня", "Фкти", "ЛЭТИ", "Питер", "Москва", "Метро", "Подвал"]
        self.password = None


    def size_check(self):
        """
        Resize images in game
        """
        h = self.app.game_screen.ui.img.height()
        self.app.game_screen.ui.img.setPixmap(self.app.img[self.state][0].scaledToHeight(h))
        self.app.game_screen.ui.text.setText(self.app.img[self.state][1])

        size = self.app.game_screen.ui.text.document().size().toSize()
        self.app.game_screen.ui.text.setFixedHeight(size.height())


    def next_state(self):
        """
        State machine for game
        """
        if self.state == 0:
            self.state += 1
            self.password = choice(self.words)
            print(f"password: [{self.password}]")
        elif self.state == 1:
            code = algorithms.Code(self.password)
            dialog = QtWidgets.QInputDialog
            text, ok = dialog.getText(self.app, 'Расшифруй', code.result)
            if ok and text:
                if text.upper() == self.password.upper():
                    self.state += 1
                else:
                    self.state += 2
        elif self.state >= 2:
            self.state = 0
            self.app.ui.stackedWidget.setCurrentIndex(0)
