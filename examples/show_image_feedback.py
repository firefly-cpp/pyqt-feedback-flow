from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget
import sys

from pyqt_feedback_flow.feedback import ImageFeedback


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
        self.button1 = QPushButton('Get feedback', self, clicked=self.send_feedback)
        layout.addWidget(self.button1)

    def send_feedback(self) -> None:
        """
        Method for showing image feedback.
        """
        self._feedback = ImageFeedback('../icons/smile.png')  # Raster image.
        # self._feedback = ImageFeedback('../icons/test.svg')  # Vector image.
        
        start = QPoint(0, 0)
        end = QPoint(500, 500)
        time = 4000
        self._feedback.show(start, end, time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ShowFeedback()
    w.show()
    sys.exit(app.exec_())