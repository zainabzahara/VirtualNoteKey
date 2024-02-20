import sys
import os

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QEvent
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QDialog, QGridLayout

class VirtualKeyboard(QDialog):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit
        self.initUI()

    def initUI(self):
        layout = QGridLayout()
        self.setLayout(layout)

        keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', '', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Windows', 'Alt', 'Space', '', '', '', 'Windows', 'Alt', 'Ctrl', '←', '↑', '↓', '→']
        ]

        for i, row in enumerate(keys):
            j = 0
            while j < len(row):
                key = row[j]
                button = QPushButton(key, self)
                if key in ('Shift', 'Caps', 'Ctrl', 'Alt', 'Windows'):
                    button.setCheckable(True)
                button.clicked.connect(lambda _, char=key: self.keyPressed(char))

                # Apply custom styling
                button.setStyleSheet("background-color: #4CAF50; color: white; font-size: 16px;")

                # Add icon (replace 'path/to/icon.png' with the actual path to your icon)
                # button.setIcon(QtGui.QIcon('path/to/icon.png'))

                # Add button to layout
                if key == 'Enter':
                    layout.addWidget(button, i, j, 1, 2)  # 1 row, 2 columns
                    j += 2
                elif key == 'Shift':
                    layout.addWidget(button, i, j, 1, 2)  # 1 row, 2 columns
                    j += 2
                elif key == 'Space':
                    button.setCheckable(True)
                    button.clicked.connect(lambda _, char='Space': self.keyPressed(char))
                    button.setFixedSize(320, 30)  # Set fixed size
                    layout.addWidget(button, i, j, 1, 4)  # 1 row, 4 columns
                    j += 4
                else:
                    layout.addWidget(button, i, j)
                    j += 1

        # Apply overall styling
        self.setStyleSheet("background-color: #233; color: #FFF; font-size: 16px;")

        self.setLayout(layout)

    def keyPressed(self, key):
        if key == 'Enter':
            self.text_edit.insertPlainText('\n')
        elif key == 'Tab':
            self.text_edit.insertPlainText('\t')
        elif key == 'Backspace':
            self.text_edit.textCursor().deletePreviousChar()
        elif key == 'Space':
            self.text_edit.insertPlainText(' ')
        else:
            self.text_edit.insertPlainText(key)

class NoteTakingApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Note-Taking Application')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.virtual_keyboard = VirtualKeyboard(self.text_edit)
        self.virtual_keyboard.hide()  # Initially hide the virtual keyboard

        # Button to toggle the virtual keyboard
        self.keyboard_button = QPushButton('Show/Hide Keyboard')
        self.keyboard_button.clicked.connect(self.toggleKeyboard)
        layout.addWidget(self.keyboard_button)
        # Apply overall color to the main window
        self.setStyleSheet("background-color: #BCFFA4;")

    # Inside the toggleKeyboard method of the NoteTakingApp class
    def toggleKeyboard(self):
        if self.virtual_keyboard.isVisible():
            self.virtual_keyboard.hide()
        else:
            self.virtual_keyboard.show()
            # Add fade animation
            self.virtual_keyboard.setWindowOpacity(0)
            self.virtual_keyboard.animation = QtCore.QPropertyAnimation(self.virtual_keyboard, b"windowOpacity")
            self.virtual_keyboard.animation.setDuration(300)
            self.virtual_keyboard.animation.setStartValue(0)
            self.virtual_keyboard.animation.setEndValue(1)
            self.virtual_keyboard.animation.start()

    def eventFilter(self, obj, event):
        if obj is self.text_edit and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_F2:
                self.toggleKeyboard()
                return True
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    os.environ["QT_IM_MODULE"] = "qtvirtualkeyboard"
    app = QApplication(sys.argv)
    note_app = NoteTakingApp()
    note_app.show()
    sys.exit(app.exec_())
