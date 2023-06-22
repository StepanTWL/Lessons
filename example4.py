"""
num = 26
print(hex(num | (1 << 7))[2:])

hex_string = '1A'
integer = int(hex_string, 16)
print(hex(integer))  # Output: 0x1a


str = "1a"
print(bytes.fromhex(str))


str = '112'
byte_array = bytearray()
print(byte_array+int(str).to_bytes(2, byteorder='big'))

import random

arr = []
begin_addr = None
end_addr = None
level = 1
for _ in range(75):
    arr.append(random.randint(0, 1))
arr = [0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
print(arr)
for i in range(len(arr)):
    if arr[i] != level:
        if begin_addr is None:
            begin_addr = i
        if end_addr is None:
            end_addr = i
        if end_addr < i:
            end_addr = i
    else:
        if end_addr is None:
            continue
        if (end_addr - begin_addr + 1) < 4:
            for j in range(begin_addr, end_addr+1):
                arr[j] = level
            begin_addr = None
            end_addr = None
        else:
            if level:
                level = 0
            else:
                level = 1
            begin_addr = i
            end_addr = i
print(arr)
"""
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QVBoxLayout, QWidget


class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Первое окно")

        self.entry = QLineEdit()
        self.button = QPushButton("Открыть второе окно")
        self.button.clicked.connect(self.open_second_window)

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(QLabel("Введите данные:"))
        layout.addWidget(self.entry)
        layout.addWidget(self.button)

        self.setCentralWidget(central_widget)

    def open_second_window(self):
        data = self.entry.text()  # Получение данных из первого окна
        second_window = SecondWindow(data)
        second_window.show()


class SecondWindow(QMainWindow):
    def __init__(self, data):
        super().__init__()
        self.setWindowTitle("Второе окно")

        self.label = QLabel(f"Данные из первого окна: {data}")

        central_widget = QWidget()
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.label)

        self.setCentralWidget(central_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    first_window = FirstWindow()
    first_window.show()
    sys.exit(app.exec())







