from app import App
import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QFontDatabase


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    font = QFontDatabase.addApplicationFont('Fairfax.ttf')
    if font == -1:
        raise FileNotFoundError("failed to connect font")

    file = QtCore.QFile(r"style.qss")
    file.open(QtCore.QIODeviceBase.OpenModeFlag.ReadOnly | QtCore.QIODeviceBase.OpenModeFlag.Text)
    stream = QtCore.QTextStream(file)
    app.setStyleSheet(stream.readAll())
    application = App()
    application.show()

    sys.exit(app.exec())