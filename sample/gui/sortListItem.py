#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 00:09
# @Author  : moiling
# @File    : sortListItemWindow.py
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from gui.pictureItem import PictureItem
from gui.ui.sortListItemWindow import Ui_Form


class SortListItem(Ui_Form, QWidget):

    # 构造函数中添加了内容设置
    def __init__(self, main_window, text):
        super().__init__()
        self.setupUi(self)

        self.main_window = main_window

        self.sortLabel.setText(text)
        self.showButton.clicked.connect(self.on_click)

        # 保存list
        self.pictureUrlList = []
        self.countPerLine = 3

    def addPicture(self, url):
        self.gridLayout.addWidget(PictureItem(self.main_window, url),
                                  len(self.pictureUrlList) / self.countPerLine,
                                  len(self.pictureUrlList) % self.countPerLine)

        self.pictureUrlList.append(url)

    @pyqtSlot()
    def on_click(self):
        if self.pictures.isHidden():
            self.pictures.show()
            self.showButton.setText('-')
        else:
            self.pictures.hide()
            self.showButton.setText('+')
