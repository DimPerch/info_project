# Form implementation generated from reading ui file 'c:\Users\Dimitry\Python programs\lab-infa\UI\start_screen.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(715, 693)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.code_button = QtWidgets.QPushButton(Form)
        self.code_button.setObjectName("code_button")
        self.menu = QtWidgets.QButtonGroup(Form)
        self.menu.setObjectName("menu")
        self.menu.addButton(self.code_button)
        self.verticalLayout_3.addWidget(self.code_button)
        self.decode_button = QtWidgets.QPushButton(Form)
        self.decode_button.setObjectName("decode_button")
        self.menu.addButton(self.decode_button)
        self.verticalLayout_3.addWidget(self.decode_button)
        self.game_button = QtWidgets.QPushButton(Form)
        self.game_button.setObjectName("game_button")
        self.verticalLayout_3.addWidget(self.game_button)
        self.about_button = QtWidgets.QPushButton(Form)
        self.about_button.setObjectName("about_button")
        self.menu.addButton(self.about_button)
        self.verticalLayout_3.addWidget(self.about_button)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 3)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 3)
        self.gridLayout.setRowStretch(2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.code_button.setText(_translate("Form", "Прямая задача"))
        self.decode_button.setText(_translate("Form", "Обратная задача"))
        self.game_button.setText(_translate("Form", "Игра"))
        self.about_button.setText(_translate("Form", "О нас"))
