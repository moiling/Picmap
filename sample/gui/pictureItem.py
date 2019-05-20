#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 00:43
# @Author  : moiling
# @File    : pictureItem.py
import os

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from gui.pictureDetail import PictureDetailWindow
from gui.ui.pictureItemWindow import Ui_Form


class PictureItem(Ui_Form, QWidget):

    # 构造函数中添加了内容设置
    def __init__(self, main_window, url):
        super().__init__()
        self.setupUi(self)

        self.url = url
        self.main_window = main_window

        pix = QPixmap(url)
        if pix.width() is not 0:
            pix = pix.scaled(200, int(pix.height() / pix.width() * 200))

        self.label.setPixmap(pix)

        self.checkBox.setText(os.path.basename(os.path.realpath(url)))

        self.label.clicked.connect(lambda: self.main_window.show_pic_details(url))
        self.label.doubleClicked.connect(lambda: self.show_picture(url))
        self.checkBox.toggled.connect(lambda: self.main_window.select_pic(url, self.checkBox.isChecked()))

    windowList = []
    @pyqtSlot()
    def show_picture(self, url):
        the_window = PictureDetailWindow(url)
        self.windowList.append(the_window)
        the_window.closed.connect(lambda: self.main_window.refresh(self.url))
        the_window.show()
