import pytest
from pytestqt.qt_compat import qt_api
from PyQt6.QtCore import QPoint, QEasingCurve
from PyQt6.QtWidgets import QApplication
from pyqt_feedback_flow import AnimationType, AnimationDirection, TextFeedback, ImageFeedback


@pytest.fixture
def widget(qtbot):
    text = "Test Notification"
    feedback = TextFeedback(text)
    qtbot.addWidget(feedback)
    return feedback

def test_text_feedback_creation(qtbot,widget):
    """
    Test that a TextFeedback instance is created with the correct text and dimensions.
    """
    text = "Test Notification"
    assert widget.text == text
    assert widget.label.text() == text
    assert widget.notification_width > 0
    assert widget.notification_height > 0

def test_animation_flow(qtbot,widget):
    """
    Test the animation flow logic for a TextFeedback instance.
    """

    screen_width = QApplication.primaryScreen().size().width()
    screen_height = QApplication.primaryScreen().size().height()
    start = QPoint(screen_width // 2, screen_height)
    end = QPoint(screen_width // 2, 0)
    time = 1000
    curve = QEasingCurve(QEasingCurve.Type.Linear)

    widget.flow(start, end, time, curve)

    assert widget.start_flow.startValue() == start
    assert widget.start_flow.endValue() == end
    assert widget.start_flow.duration() == time
    assert widget.start_flow.easingCurve().type() == QEasingCurve.Type.Linear
