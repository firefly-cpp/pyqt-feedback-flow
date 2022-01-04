from pyqt_feedback_flow.feedback import Feedback
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QPushButton
import sys
import time
import random
import emoji


class ShowFeedback(QWidget):

    def __init__(self):
        super(ShowFeedback, self).__init__()
        layout = QVBoxLayout(self)
        self.button1 = QPushButton(
            "Get feedback: ", self, clicked=self.send_feedback)
        layout.addWidget(self.button1)

    def send_feedback(self):
        self._feedback = Feedback(img = "icons/smile.png")
        self._feedback.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = ShowFeedback()
    w.show()
    sys.exit(app.exec_())

