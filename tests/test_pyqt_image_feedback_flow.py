import pytest
from pytestqt.qt_compat import qt_api
from PyQt6.QtCore import QPoint, QEasingCurve
from PyQt6.QtWidgets import QApplication
from pyqt_feedback_flow import AnimationType, AnimationDirection, TextFeedback, ImageFeedback

def widget(qtbot,tmp_path):
    svg_path = tmp_path / "test.svg"
    svg_path.write_text('<svg xmlns="http://www.w3.org/2000/svg" width="100" height="100"><rect width="100" height="100" style="fill:blue;"/></svg>')

    feedback = ImageFeedback(str(svg_path), 100, 100)
    qtbot.addWidget(feedback)
    return feedback


def test_image_feedback_creation_svg(qtbot,widget):
    """
    Test that an ImageFeedback instance is created correctly for an SVG file.
    """    

    assert widget.vector is not None
    assert widget.vector.width() == 100
    assert widget.vector.height() == 100
