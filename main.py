import sys
import random

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.pushButton.setHidden(True),
        while True:
            time.sleep(1000)
            r = random.randrange(0, 600)
            self.circle.move(random.randrange(0, 600), random.randrange(0, 600))
            self.circle.resize(r, r)
            self.label_1.setStyleSheet("border: 3px solid yellow;
                                    border-radius: %dpx;" % r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
