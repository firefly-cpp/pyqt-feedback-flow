import pytest
from PyQt6.QtCore import QPoint, QEasingCurve
from PyQt6.QtWidgets import QApplication
from pyqt_feedback_flow import AnimationType, AnimationDirection, TextFeedback, ImageFeedback


def test_text_feedback_creation(qtbot):
    """
    Test that a TextFeedback instance is created with the correct text and dimensions.
    """
    text = "Test Notification"
    feedback = TextFeedback(text)
    qtbot.addWidget(feedback)

    assert feedback.text == text
    assert feedback.label.text() == text
    assert feedback.notification_width > 0
    assert feedback.notification_height > 0


def test_image_feedback_creation_svg(qtbot, tmp_path):
    """
    Test that an ImageFeedback instance is created correctly for an SVG file.
    """
    svg_path = tmp_path / "test.svg"
    svg_path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><rect width="100" height="100" style="fill:blue;"/></svg>')

    feedback = ImageFeedback(str(svg_path), 100, 100)
    qtbot.addWidget(feedback)

    assert feedback.vector is not None
    assert feedback.vector.width() == 100
    assert feedback.vector.height() == 100


def test_animation_flow(qtbot):
    """
    Test the animation flow logic for a TextFeedback instance.
    """
    feedback = TextFeedback("Test Animation")
    qtbot.addWidget(feedback)

    screen_width = QApplication.primaryScreen().size().width()
    screen_height = QApplication.primaryScreen().size().height()
    start = QPoint(screen_width // 2, screen_height)
    end = QPoint(screen_width // 2, 0)
    time = 1000
    curve = QEasingCurve(QEasingCurve.Type.Linear)

    feedback.flow(start, end, time, curve)

    assert feedback.start_flow.startValue() == start
    assert feedback.start_flow.endValue() == end
    assert feedback.start_flow.duration() == time
    assert feedback.start_flow.easingCurve().type() == QEasingCurve.Type.Linear
