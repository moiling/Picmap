#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-19 22:54
# @Author  : moiling
# @File    : main.py
import sys

from gui.ui.mainWindow import Ui_MainWindow
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())
