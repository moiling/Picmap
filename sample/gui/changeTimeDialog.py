#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 06:28
# @Author  : moiling
# @File    : changeTimeDialog.py
from PyQt5.QtWidgets import QDialog

from gui.ui.changeTimeDialogWindow import Ui_Dialog


class ChangeTimeDialog(Ui_Dialog, QDialog):

    # 构造函数中添加了内容设置
    def __init__(self, exif):
        super().__init__()
        self.setupUi(self)

        stt, sty, end = exif.pic_time()
        if stt is not None:
            self.startTimeEdit.setText(str(stt))
        else:
            self.startTimeEdit.setText(str(0))

        if sty is not None:
            self.stayTimeEdit.setText(str(sty))
        else:
            self.stayTimeEdit.setText(str(0))

        if end is not None:
            self.endTimeEdit.setText(str(end))
        else:
            self.endTimeEdit.setText(str(1440))


