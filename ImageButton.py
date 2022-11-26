from pathlib import Path

import PySide6
from PySide6.QtGui import QPainter, QPixmap
from PySide6.QtWidgets import QPushButton


class ImageButton(QPushButton):
    def __init__(self, image_path: Path, width: int, height: int, intent=5, parent=None):
        super(ImageButton, self).__init__(parent)
        self.pixmap = QPixmap(str(image_path.absolute()))
        self.w, self.h, self.i = width, height, intent
        self.setFixedSize(width, height)
        print(self.pixmap)

    def update_image(self, image_path: Path):
        self.pixmap = QPixmap(str(image_path.absolute()))

    def paintEvent(self, a0: PySide6.QtGui.QPaintEvent) -> None:
        super(ImageButton, self).paintEvent(a0)
        qp = QPainter()
        qp.begin(self)
        qp.drawPixmap(self.i, self.i, self.w - self.i * 2, self.w - self.i * 2, self.pixmap)
        qp.end()
