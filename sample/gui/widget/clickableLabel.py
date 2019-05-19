#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 01:13
# @Author  : moiling
# @File    : clickableLabel.py
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ClickableLabel(QLabel):
    clicked = pyqtSignal()
    doubleClicked = pyqtSignal()

    def mouseDoubleClickEvent(self, e):
        self.doubleClicked.emit()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.clicked.emit()
