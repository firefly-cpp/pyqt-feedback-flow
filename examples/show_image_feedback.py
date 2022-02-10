from PyQt5.QtCore import QEasingCurve
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys

from pyqt_feedback_flow.feedback import AnimationType, ImageFeedback


class ShowFeedback(QWidget):
    """
    Class for showing feedback on screen in the form of an image toast notification.
    """
    def __init__(self) -> None:
        """
        Initialisation method for ShowFeedback class.
        """
        super(ShowFeedback, self).__init__()
        
        layout = QVBoxLayout(self)
        self.button1 = QPushButton('Get vertical feedback', self)
        self.button1.clicked.connect(lambda: self.send_feedback(AnimationType.VERTICAL))
        layout.addWidget(self.button1)

        self.button2 = QPushButton('Get horizontal feedback', self)
        self.button2.clicked.connect(lambda: self.send_feedback(AnimationType.HORIZONTAL))
        layout.addWidget(self.button2)

        self.button3 = QPushButton('Get diagonal feedback', self)
        self.button3.clicked.connect(lambda: self.send_feedback(AnimationType.MAIN_DIAGONAL))
        layout.addWidget(self.button3)

        self.button4 = QPushButton('Get antidiagonal feedback', self)
        self.button4.clicked.connect(lambda: self.send_feedback(AnimationType.ANTI_DIAGONAL))
        layout.addWidget(self.button4)

    def send_feedback(self, type_of_animation: int) -> None:
        """
        Method for showing image feedback.\n
        Args:
            type_of_animation (int): one of the preset types of animations in AnimationType enum class
        """
        icon_width = 100
        icon_height = 100
        self._feedback = ImageFeedback('../icons/svg/smile.svg', width=icon_width, height=icon_height)
        
        time = 3000
        self._feedback.show(type_of_animation, time, QEasingCurve.InQuad)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ShowFeedback()
    w.show()
    sys.exit(app.exec_())