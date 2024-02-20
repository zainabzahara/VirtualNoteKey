#<<<<<<--------xxxxx----Final orientation fixed of keyboard----xxxx-------->>>>


from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QTextEdit, QLineEdit

class Keyboard(QDialog):
    def __init__(self, text_edit):
        super().__init__()
        self.text_edit = text_edit
        self.shiftPressed = False
        self.capsPressed = False
        self.ctrlPressed = False
        self.altPressed = False
        self.windowsPressed = False
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        keys = [
            ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'Backspace'],
            ['Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\'],
            ['Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'', 'Enter'],
            ['Shift', '', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'Shift'],
            ['Ctrl', 'Windows', 'Alt', 'Space','','','', 'Windows','Alt', 'Ctrl', '←', '↑', '↓', '→']
        ]

        for i, row in enumerate(keys):
            j = 0
            while j < len(row):
                key = row[j]
                button = QPushButton(key, self)
                if key in ('Shift', 'Caps', 'Ctrl', 'Alt', 'Windows'):
                    button.setCheckable(True)
                button.clicked.connect(lambda _, char=key: self.keyPressed(char))

                # Adjust size and placement for specific buttons
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

        self.setLayout(layout)

    def keyPressed(self, key):
        if key in ('Shift', 'Caps', 'Ctrl', 'Alt', 'Windows'):
            state = not getattr(self, f'{key.lower()}Pressed')
            setattr(self, f'{key.lower()}Pressed', state)
            print(f'{key} Pressed:', state)

            # Handle state changes for Shift, Caps, Ctrl, and Alt
            if key == 'Shift':
                self.handleShiftState(state)
            elif key == 'Caps':
                self.handleCapsState(state)
            elif key == 'Ctrl':
                self.handleCtrlState(state)
            elif key == 'Alt':
                self.handleAltState(state)
            elif key == 'Windows':
                self.handleWindowsState(state)

        elif key == 'Enter':
            self.text_edit.insert('\n')
        elif key == 'Tab':
            self.text_edit.insert('\t')
        elif key == 'Space':
            self.text_edit.insert(' ')
        elif key == 'Backspace':
            if isinstance(self.text_edit, QTextEdit):
                cursor = self.text_edit.textCursor()
                cursor.deletePreviousChar()
                self.text_edit.setTextCursor(cursor)
            elif isinstance(self.text_edit, QLineEdit):
                text = self.text_edit.text()
                self.text_edit.setText(text[:-1])
        elif key in ('←', '↑', '↓', '→'):
            print(f'Arrow Key: {key}')
        else:
            if key not in ('Shift', 'Caps', 'Ctrl', 'Alt', 'Windows'):
                if key.isalpha() and (self.shiftPressed or self.capsPressed):
                    self.text_edit.insert(key.upper())
                else:
                    self.text_edit.insert(key.lower())

    def handleShiftState(self, state):
        # Implement the logic to handle Shift state changes
        print('Shift State:', state)

    def handleCapsState(self, state):
        # Implement the logic to handle Caps state changes
        print('Caps State:', state)

    def handleCtrlState(self, state):
        # Implement the logic to handle Ctrl state changes
        print('Ctrl State:', state)

    def handleAltState(self, state):
        # Implement the logic to handle Alt state changes
        print('Alt State:', state)
    def handleWindowsState(self, state):
        # Implement the logic to handle Alt state changes
        print('Windows State:', state)