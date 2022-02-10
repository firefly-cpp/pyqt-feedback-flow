from enum import auto, Enum
from PyQt5.QtCore import QEasingCurve, QPoint, QPropertyAnimation, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget


class AnimationType(Enum):
    """
    Enumeration class for the type of animation. 
    """
    VERTICAL = 0
    HORIZONTAL = 1
    MAIN_DIAGONAL = 2
    ANTI_DIAGONAL = 3


class _Feedback(QWidget):
    """
    Abstract class for giving feedback in the form of toast notifications.
    """
    def __init__(self, width: int = 100, height: int = 100) -> None:
        """
        Initialisation method for Feedback class.\n
        Args:
            width (int): width of the notification
            height (int): height of the notification
        """
        super(_Feedback, self).__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.X11BypassWindowManagerHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.layout = QVBoxLayout(self)
        self.notification_width = width
        self.notification_height = height
            
    def show(self, type_of_animation: int, time: int = 3000, curve: int = QEasingCurve.OutInQuart) -> None:
        """
        Method for displaying a toast notification.\n
        Args:
            type_of_animation (int): one of the preset types of animations in AnimationType enum class
            time (int): desired time of the flow in milliseconds
            curve (int): the type of easing curve of the animation
        """
        # Obtaining the screen size.
        screen = QApplication.primaryScreen().size()
        width = screen.width()
        height = screen.height()

        # Vertical animation.
        if type_of_animation == AnimationType.VERTICAL:
            start = QPoint(width // 2 - self.notification_width // 2, height - self.notification_height)
            end = QPoint(width // 2 - self.notification_width // 2, 0)
        # Horizontal animation.
        elif type_of_animation == AnimationType.HORIZONTAL:
            start = QPoint(0, height // 2 - self.notification_height // 2)
            end = QPoint(width - self.notification_width, height // 2 - self.notification_height // 2)
        # Main diagonal animation.
        elif type_of_animation == AnimationType.MAIN_DIAGONAL:
            start = QPoint(width - self.notification_width, height - self.notification_height)
            end = QPoint(0, 0)
        # Antidiagonal animation.
        elif type_of_animation == AnimationType.ANTI_DIAGONAL:
            start = QPoint(0, height - self.notification_height)
            end = QPoint(width - self.notification_width, 0)

        super(_Feedback, self).show()
        self.flow(start, end, time, curve)

    def flow(self, start: QPoint, end: QPoint, time: int, curve: int) -> None:
        """
        Method for a notification to flow from start point to end point.\n
        Args:
            start (QPoint): starting point
            end (QPoint): ending point
            time (int): desired time of the flow in milliseconds
            curve (int): the type of easing curve of the animation
        """
        # Animation of the position of the notification.
        self.start_flow = QPropertyAnimation(self, b'pos')
        self.start_flow.setStartValue(start)
        self.start_flow.setEndValue(end)
        self.start_flow.setEasingCurve(curve)
        self.start_flow.setDuration(time)
        self.start_flow.finished.connect(self.close)

        # Animation of the opacity of the notification.
        self.start_opacity = QPropertyAnimation(self, b'windowOpacity')
        self.start_opacity.setStartValue(1)
        self.start_opacity.setEndValue(0)
        self.start_opacity.setEasingCurve(QEasingCurve.InQuint)
        self.start_opacity.setDuration(time)

        self.start_flow.start()
        self.start_opacity.start()


class ImageFeedback(_Feedback):
    """
    Class for giving image feedback in the form of toast notifications.\n
    Args:
        img (str): path to the image
        width (int): width of the image
        height (int): height of the image
    """
    def __init__(self, img: str, width: int, height: int) -> None:
        """
        Initialisation method for ImageFeedback class.\n
        Args:
            img (str): path to the image
            width (int): width of the image
            height (int): height of the image
        """
        super(ImageFeedback, self).__init__(width, height)
        self.img = img

        format = self.img.rsplit('.')[-1]  # Obtaining the format of the image.

        # If the format of the image is SVG, the image has to be opened with QSvgWidget.
        if format == 'svg':
            self.vector = QSvgWidget(self.img)
            self.vector.setFixedSize(width, height)
            self.layout.addWidget(self.vector)
        # If the image is raster, it is opened with QPixmap.
        else:
            pixmap = QPixmap(self.img).scaled(width, height, transformMode=Qt.SmoothTransformation)
            self.label = QLabel(self)
            self.layout.addWidget(self.label)
            self.label.setPixmap(pixmap)


class TextFeedback(_Feedback):
    """
    Class for giving text feedback in the form of toast notifications.\n
    Args:
        text (str): text to be displayed
    """
    def __init__(self, text: str) -> None:
        """
        Initialisation method for ImageFeedback class.\n
        Args:
            img (str): path to the image
        """
        super(TextFeedback, self).__init__()
        self.text = text
        self.label = QLabel(self)
        self.layout.addWidget(self.label)
        self.label.setStyleSheet('background-color: white;\
                                  font-size: 18pt;\
                                  padding: 20px;\
                                  border: 1px solid black;\
                                  border-radius: 15px;\
                                  font-family: Bahnschrift SemiLight')
        self.label.setText(self.text)
        self.label.adjustSize()
        self.notification_width = self.label.width()
        self.notification_height = self.label.height()