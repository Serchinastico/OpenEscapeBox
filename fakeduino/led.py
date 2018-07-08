from .fakeduino import FakeduinoComponent
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QWidget


class LedComponent(QWidget, FakeduinoComponent):
    def __init__(self):
        super().__init__()
        self._value = False

    def paintEvent(self, event):
        paint_rect = event.rect()
        radius = (min(paint_rect.height(), paint_rect.width()) - 2) / 2

        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.green if self._value else Qt.gray)
        painter.drawEllipse(paint_rect.width() / 2,
                            paint_rect.height() / 2, radius, radius)
        painter.end()

    def minimumSizeHint(self):
        return QSize(25, 25)

    def writePin(self, value):
        self._value = value
        self.update()
