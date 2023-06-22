import sys
from PyQt5.Qt import *


class Dialog(QDialog):
    dataChanged = pyqtSignal(str)

    def __init__(self, parent=None):
        QDialog.__init__(self)
        self.btnApply = QPushButton(u'Применить')
        self.btnOK = QPushButton(u'Закрыть')
        self.line = QLineEdit()
        grid = QGridLayout(self)
        grid.addWidget(self.line, 0, 0, 1, 3)
        grid.addWidget(self.btnOK, 1, 1)
        grid.addWidget(self.btnApply, 1, 2)
        self.btnOK.clicked.connect(self.accept)
        self.btnApply.clicked.connect(self.getData)
        self.line.setFocus()

    def getData(self):
        self.dataChanged.emit(self.line.text())


class W(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.btn = QPushButton("Push")
        self.line = QLineEdit()
        grid = QGridLayout(self)
        grid.addWidget(self.line, 0, 0)
        grid.addWidget(self.btn, 1, 0)
        self.btn.clicked.connect(self.btnClick)

    def btnClick(self):
        d = Dialog()
        d.dataChanged.connect(self.setData)
        d.exec_()
        d.dataChanged.disconnect(self.setData)
        del d

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