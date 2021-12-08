from app import App
import sys
from PyQt5 import QtWidgets


app = QtWidgets.QApplication([])
application = App()
application.show()


sys.exit(app.exec())