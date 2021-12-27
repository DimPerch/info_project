from app import App
import sys
from PyQt6 import QtWidgets


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = App()
    application.show()

    sys.exit(app.exec())