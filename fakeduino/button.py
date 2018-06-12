from .fakeduino import FakeduinoComponent
from PyQt5.QtWidgets import QPushButton


class ButtonComponent(QPushButton, FakeduinoComponent):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        self._value = 1

    def mouseReleaseEvent(self, event):
        super().mouseReleaseEvent(event)
        self._value = 0
