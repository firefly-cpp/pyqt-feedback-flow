from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt, QPoint, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt5.QtGui import QIcon, QPixmap


class Feedback(QWidget):

    def __init__(self, img=None, text=None):
        super(Feedback, self).__init__()
        self.img = img
        self.text = text

        self.setWindowFlags(Qt.FramelessWindowHint |
                            Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)

        layout = QVBoxLayout(self)

        # show text
        if self.text is not None:
            self.setMinimumWidth(220)
            self.setMinimumHeight(70)
            self.label = QLabel(self)
            layout.addWidget(self.label)
            self.label.setStyleSheet(
                "background-color: white; border: 1px solid black;")

            self.label.setText(self.text)

        # show image
        if self.img is not None:
            self.setMinimumWidth(100)
            self.setMinimumHeight(100)
            self.label = QLabel(self)
            layout.addWidget(self.label)
            pixmap = QPixmap(self.img)
            pixmap2 = pixmap.scaledToWidth(100)
            #pixmap3 = pixmap.scaledToHeight(64)
            self.label.setPixmap(pixmap2)
            self.label.show()


    def show(self):
        super(Feedback, self).show()
        self.flow(QPoint(0, 25), QPoint(100, 250))

    def flow(self, start, end):
        self.start_flow = QPropertyAnimation(self, b"pos")
        self.start_flow.setStartValue(start)
        self.start_flow.setEndValue(end)
        self.start_flow.setEasingCurve(QEasingCurve.InQuad)
        self.start_flow.setDuration(3000)
        self.start_flow.finished.connect(self.close)
        self.start_flow.start()
