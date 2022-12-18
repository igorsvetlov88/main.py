import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor, QBrush
from PyQt5.QtWidgets import QApplication, QWidget
from random import randint


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.initUI()

    def initUI(self):
        self.new_circles = False
        self.setWindowTitle('Желтые окружности')
        self.pushButton.clicked.connect(self.drawing)

    def drawing(self):
        self.new_circles = True
        self.repaint()

    def paintEvent(self, event):
        if self.new_circles:
            self.new_circles = False
            self.qp = QPainter()
            self.qp.begin(self)
            self.qp.setBrush(QColor(255, 255, 0))
            for x in range(randint(2, 5)):
                rnd_size = randint(10, 200)
                self.qp.drawEllipse(randint(0, self.width() - rnd_size),
                                    randint(0, self.height() - rnd_size), rnd_size, rnd_size)
            self.qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
