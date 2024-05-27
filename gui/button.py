from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QApplication, QTableWidgetItem, QWidget, QVBoxLayout

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.setFocusPolicy(
            Qt.StrongFocus
        )  # Ensure the button can receive keyboard focus
        # self.clicked.connect(self.on_click)

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter, Qt.Key_Space):

            self.click()
        else:
            super().keyPressEvent(event)

    # def on_click(self):
        # print("Button clicked!")


class TableWidget(QTableWidget):
    def keyPressEvent(self, event):
        key = event.key()
        if key == Qt.Key_Tab:
            print("Натиснено", key)
            if event.modifiers() & Qt.ShiftModifier:
                widget = self.focusNextPrevChild(False)
            else:
                widget = self.focusNextPrevChild(True)  # Перемістити фокус на наступний віджет
            if widget:
                widget.setFocus()
                return
        super().keyPressEvent(event)  # Для всіх інших клавіш викликається стандартна обробка

