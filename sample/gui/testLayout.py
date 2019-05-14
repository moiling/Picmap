#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-14 13:57
# @Author  : moiling
# @File    : testLayoutUI.py
import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets, QtGui

from gui.testListWidget import TestListWidget
from gui.ui.testLayoutUI import Ui_TestLayout


class TestLayout(Ui_TestLayout, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.addWidget()

    def addWidget(self):
        # 这里注意要给Content添加一个layout，在layout中添加子控件
        # 这好像是Mac的qt ui设计的bug，没法在空widget中添加layout，必须手动添加
        # Win我记得好像空的可以添加
        pic_url = ('../test/pic/a.jpg', '../test/pic/b.jpg', '../test/pic/c.jpg',
                   '../test/pic/d.jpg', '../test/pic/e.jpg')

        # 添加子控件
        for i in range(10):
            self.formLayout.addWidget(TestListWidget(pic_url[i % len(pic_url)], 'Button' + str(i)))

    def dragEnterEvent(self, evn):
        evn.accept()

    def dropEvent(self, evn: QtGui.QDropEvent):
        file_url = evn.mimeData().text()
        if file_url[:7] != 'file://':
            return

        if file_url[9] == ':':
            # file:///C:,第9位是:的大概就是windows了
            img_url = evn.mimeData().text()[8:]
        else:
            img_url = evn.mimeData().text()[7:]

        # 显示图片
        self.formLayout.addWidget(TestListWidget(img_url, 'add'))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = TestLayout()
    test.show()
    sys.exit(app.exec_())



