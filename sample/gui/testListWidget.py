#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-14 13:59
# @Author  : moiling
# @File    : testListWidget.py
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget

from gui.ui.testListWidgetUI import Ui_TestListWidget


class TestListWidget(Ui_TestListWidget, QWidget):

    # 构造函数中添加了内容设置
    def __init__(self, pic, text):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

        # 通过构造函数的参数，添加图片和文字
        pix = QPixmap(pic)

        if pix.width() is not 0:
            pix = pix.scaled(200, int(pix.height() / pix.width() * 200))

        self.label.setPixmap(pix)
        self.pushButton.setText(text)
        # 添加点击事件
        self.text = text
        self.pushButton.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print(self.text, ' button click')
