from PyQt5.QtCore import QEasingCurve, QPoint, QPropertyAnimation, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget


class Feedback(QWidget):
    """
    Abstract class for giving feedback in the form of toast notifications.
    """
    def __init__(self) -> None:
        """
        Initialisation method for Feedback class.
        """
        super(Feedback, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)
        self.layout = QVBoxLayout(self)
            
    def show(self, start: QPoint, end: QPoint, time: int = 3000) -> None:
        """
        Method for displaying a toast notification.\n
        Args:
            start (QPoint): starting point
            end (QPoint): ending point
            time (int): desired time of the flow in milliseconds
        """
        super(Feedback, self).show()
        self.flow(start, end, time)

    def flow(self, start: QPoint, end: QPoint, time: int) -> None:
        """
        Method for a notification to flow from start point to end point.\n
        Args:
            start (QPoint): starting point
            end (QPoint): ending point
            time (int): desired time of the flow in milliseconds
        """
        self.start_flow = QPropertyAnimation(self, b"pos")
        self.start_flow.setStartValue(start)
        self.start_flow.setEndValue(end)
        self.start_flow.setEasingCurve(QEasingCurve.InQuad)
        self.start_flow.setDuration(time)
        self.start_flow.finished.connect(self.close)
        self.start_flow.start()


class ImageFeedback(Feedback):
    """
    Class for giving image feedback in the form of toast notifications.
    Args:
        img (str): path to the image
        width (int): width of the image
        height (int): height of the image
    """
    def __init__(self, img: str, width: int = 100, height: int = 100) -> None:
        """
        Initialisation method for ImageFeedback class.\n
        Args:
            img (str): path to the image
            width (int): width of the image
            height (int): height of the image
        """
        super(ImageFeedback, self).__init__()
        self.img = img
        pixmap = QPixmap(self.img).scaled(width, height, transformMode=Qt.SmoothTransformation)

        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        self.label.setPixmap(pixmap)


class TextFeedback(Feedback):
    """
    Class for giving text feedback in the form of toast notifications.
    Args:
        text (str): text to be displayed
    """
    def __init__(self, text: str) -> None:
        """
        Initialisation method for ImageFeedback class.
        Args:
            img (str): path to the image
        """
        super(TextFeedback, self).__init__()
        self.text = text
        
        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        self.label.setStyleSheet("background-color: white; border: 1px solid black;")
        self.label.setText(self.text)