# pyqt-feedback-flow --- Show feedbacks in toast-like notifications

---

[![PyPI Version](https://img.shields.io/pypi/v/pyqt-feedback-flow.svg)](https://pypi.python.org/pypi/pyqt-feedback-flow)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyqt-feedback-flow.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/pyqt-feedback-flow.svg)
[![Downloads](https://pepy.tech/badge/pyqt-feedback-flow)](https://pepy.tech/project/pyqt-feedback-flow)
[![GitHub license](https://img.shields.io/github/license/firefly-cpp/pyqt-feedback-flow.svg)](https://github.com/firefly-cpp/pyqt-feedback-flow/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/pyqt-feedback-flow.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/pyqt-feedback-flow.svg)](http://isitmaintained.com/project/firefly-cpp/pyqt-feedback-flow "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/firefly-cpp/pyqt-feedback-flow.svg)](http://isitmaintained.com/project/firefly-cpp/pyqt-feedback-flow "Percentage of issues still open")
[![Fedora package](https://img.shields.io/fedora/v/python3-pyqt-feedback-flow?color=blue&label=Fedora%20Linux&logo=fedora)](https://src.fedoraproject.org/rpms/python-pyqt-feedback-flow)

## Motivation
This is a very simple module that was developed as a part of our [AST application](https://arxiv.org/pdf/2109.13334.pdf) for showing simple notifications during the cycling training sessions, in order to pass on a cyclist`s essential information, as well as information that can be submitted by a sport trainer.

This software allows us to show notification in the realm of a text or a picture. It was shown that flowing feedback is
more appropriate for a cyclist than static notification or pop up windows. It was tailored to our project, but the project can easily be adjusted for particular special needs. It can also be integrated into existing PyQt projects very easily.

It was not intended to be released as a separate module, but it may inspire someone to provide updates
or extensions to this module. Currently, the project is still very immature. It was just used in simple
practical tests with our AST-GUI.

## Installation

### pip

Install this software with pip:

```sh
pip install pyqt-feedback-flow
```

### Arch Linux

To install pyqt-feedback-flow on Arch Linux, please use an [AUR helper](https://wiki.archlinux.org/title/AUR_helpers):

```sh
$ yay -Syyu python-pyqt-feedback-flow
```

## License

This package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!
