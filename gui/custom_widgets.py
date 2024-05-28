from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QApplication, QTableWidgetItem, QWidget, QVBoxLayout

class Button(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        # Ensure the button can receive keyboard focus
        # self.setFocusPolicy(
            # Qt.StrongFocus
        # ) 

    def keyPressEvent(self, event):
        if event.key() in (Qt.Key_Return, Qt.Key_Enter, Qt.Key_Space):
            self.click()
        else:
            super().keyPressEvent(event)


class TableWidget(QTableWidget):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.setEditTriggers(self.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.resizeColumnsToContents()
        self.resizeRowsToContents()
    
    def keyPressEvent(self, event):
        if int(event.key()) == 16777218:
            self.parent.focusNextPrevChild(False)
        elif int(event.key()) == 16777217:
            self.parent.focusNextPrevChild(True)
        else:
            super().keyPressEvent(event)

