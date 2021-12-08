from app import App
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QFontDatabase


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    font = QFontDatabase.addApplicationFont('Fairfax.ttf')
    if font == -1:
        raise FileNotFoundError("failed to connect font")

    file = QtCore.QFile(r"style.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())

    application = App()
    application.show()

    sys.exit(app.exec())