from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)        
        self.setFocusPolicy(Qt.StrongFocus)  # Ensure the button can receive keyboard focus
        self.clicked.connect(self.on_click)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter, Qt.Key_Space):
            
            self.click()
        else:
            super().keyPressEvent(event)

    def on_click(self):
        print("Button clicked!")
