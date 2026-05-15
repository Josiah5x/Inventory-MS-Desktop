import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QCalendarWidget, QDialog
)
from PyQt5.QtCore import Qt, QDate


class CalendarPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowFlags(Qt.Popup)
        self.setFixedSize(300, 250)

        layout = QVBoxLayout(self)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)

        layout.addWidget(self.calendar)


class DateLineEdit(QLineEdit):
    def __init__(self):
        super().__init__()

        self.setPlaceholderText("Click to select date")
        self.calendar_popup = CalendarPopup(self)

        # Select date from calendar
        self.calendar_popup.calendar.clicked.connect(self.set_date)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)

        # Position popup below QLineEdit
        pos = self.mapToGlobal(self.rect().bottomLeft())
        self.calendar_popup.move(pos)

        # Show popup
        self.calendar_popup.show()

    def set_date(self, date):
        self.setText(date.toString("dd/MM/yyyy"))
        self.calendar_popup.hide()


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QLineEdit Calendar Popup")
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.date_input = DateLineEdit()

        layout.addWidget(self.date_input)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec_())