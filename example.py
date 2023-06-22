from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_first1(object):
    def setupUi(self, first1):
        first1.setObjectName("first1")
        first1.resize(580, 449)
        self.label = QtWidgets.QLabel(first1)
        self.label.setGeometry(QtCore.QRect(160, 40, 191, 71))
        self.label.setObjectName("label")
        self.retranslateUi(first1)
        QtCore.QMetaObject.connectSlotsByName(first1)

    def retranslateUi(self, first1):
        _translate = QtCore.QCoreApplication.translate
        first1.setWindowTitle(_translate("first1", "Form"))
        self.label.setText(_translate("first1", "first windows"))


class Ui_second2(object):
    def setupUi(self, second2):
        second2.setObjectName("second2")
        second2.resize(294, 200)
        self.label = QtWidgets.QLabel(second2)
        self.label.setGeometry(QtCore.QRect(50, 120, 191, 71))
        self.label.setObjectName("label")
        self.retranslateUi(second2)
        QtCore.QMetaObject.connectSlotsByName(second2)

    def retranslateUi(self, second2):
        _translate = QtCore.QCoreApplication.translate
        second2.setWindowTitle(_translate("second2", "Form"))
        self.label.setText(_translate("second2", "second windows"))


class SecondWindow(QtWidgets.QWidget, Ui_second2):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent, QtCore.Qt.Window)
        self.setupUi(self)
        self.parent = parent

    def closeEvent(self, event):
        print("close SecondWindow и вызвать функцию ")
        self.parent.my_func("Hello World")


class FirstWindow(QtWidgets.QWidget, Ui_first1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.second = SecondWindow(self)
        self.second.show()

    def closeEvent(self, event):
        print("close FirstWindow ")

    def my_func(self, text):
        print(text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = FirstWindow()
    w.show()
    sys.exit(app.exec_())