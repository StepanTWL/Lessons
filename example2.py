import sys
from PyQt5.Qt import *
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QLineEdit, QGridLayout, QPushButton, QApplication


class View(QWidget):
    dataChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.line = QLineEdit()
        grid = QGridLayout(self)
        grid.addWidget(self.line, 0, 0, 1, 3)
        self.arr = [0]*8

    def closeEvent(self, event):
        print(''.join([str(x) for x in self.arr]))
        self.dataChanged.emit(' '.join([str(x) for x in self.arr]))


class W(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.btn = QPushButton("Push")
        self.line = QLineEdit()
        grid = QGridLayout(self)
        grid.addWidget(self.line, 0, 0)
        grid.addWidget(self.btn, 1, 0)
        self.btn.clicked.connect(self.btnClick)
        self.view = View()
        self.view.dataChanged.connect(self.setData)

    def btnClick(self):
        self.view.show()

    def setData(self, data):
        self.line.setText(data)


def app_quit():
    sys.exit()


if __name__ == "__main__":
    app = QApplication([])
    app.lastWindowClosed.connect(app_quit)
    w = W()
    w.show()
    app.exec_()