# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverclientdesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 327)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(40, 40, 291, 240))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_variant_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_variant_2.setObjectName("label_variant_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_variant_2)
        self.label_problem = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_problem.setObjectName("label_problem")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_problem)
        self.spin_problem = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spin_problem.setObjectName("spin_problem")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spin_problem)
        self.spin_variant = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spin_variant.setObjectName("spin_variant")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.spin_variant)
        self.label_score = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_score.setObjectName("label_score")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_score)
        self.spin_score = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spin_score.setObjectName("spin_score")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spin_score)
        self.textEdit_output = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_output.setObjectName("textEdit_output")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.textEdit_output)
        self.label_output = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_output.setObjectName("label_output")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_output)
        self.add_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.add_button.setObjectName("add_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.add_button)
        self.delete_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.delete_button.setObjectName("delete_button")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.delete_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SGContest Server"))
        self.label_variant_2.setText(_translate("MainWindow", "Вариант"))
        self.label_problem.setText(_translate("MainWindow", "Задача"))
        self.label_score.setText(_translate("MainWindow", "Оценка"))
        self.label_output.setText(_translate("MainWindow", "Ожидаемый вывод"))
        self.add_button.setText(_translate("MainWindow", "Добавить"))
        self.delete_button.setText(_translate("MainWindow", "Удалить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())