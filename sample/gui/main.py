#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-19 22:54
# @Author  : moiling
# @File    : main.py
import os
import sys
import time

import apiRequest

from exif import Exif
from gui.bean.pic import Pic
from gui.sortListItem import SortListItem
from gui.ui.mainWindow import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui


class MainWindow(Ui_MainWindow, QMainWindow):

    pic_list = []
    sort_type = 1
    sort_item_list = []  # 分组的保存

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)
        self.detailWidget.hide()
        self.hiddenButton.clicked.connect(self.hide_pic_details)
        self.sortComboBox.setCurrentIndex(self.sort_type)
        self.sortComboBox.currentIndexChanged.connect(self.set_sort_type)

    def dragEnterEvent(self, evn):
        evn.accept()

    def dropEvent(self, evn: QtGui.QDropEvent):
        file_urls = evn.mimeData().text().split('\n')
        print(file_urls)
        for file_url in file_urls:
            if file_url == '':
                continue

            if file_url[:7] != 'file://':
                # TODO 显示失败原因在界面上
                break
            if file_url[9] == ':':
                # file:///C:,第9位是:的大概就是windows了
                img_url = file_url[8:]
            else:
                img_url = file_url[7:]

            # 读Exif信息
            e = Exif(img_url)

            if not e.succeed:
                # TODO 显示失败原因在界面上
                break

            longitude, latitude = e.location()

            if not e.succeed:
                # TODO 显示失败原因在界面上
                break

            # 转换成地点信息
            country, province, city = apiRequest.re_geocode(longitude, latitude)

            if type(city) is str:
                location_str = country + ' ' + province + ' ' + city
            else:
                location_str = country + ' ' + province

            pic = Pic(img_url, location_str, time.ctime(os.path.getctime(img_url)))
            self.pic_list.append(pic)
            self.showPic(pic)

    @pyqtSlot()
    def show_pic_details(self, url):
        self.detailWidget.show()
        self.nameText.setText(os.path.basename(os.path.realpath(url)))
        self.urlText.setText(url)
        # TODO
        self.locationText.setText('测试地点')
        self.timeText.setText('测试时间')

    @pyqtSlot()
    def hide_pic_details(self):
        self.detailWidget.hide()

    @pyqtSlot()
    def set_sort_type(self):
        self.sort_type = self.sortComboBox.currentIndex()
        self.refresh()

    def refresh(self):
        # 清空
        for s in self.sort_item_list:
            self.formLayout.removeWidget(s)
            s.deleteLater()

        self.sort_item_list.clear()

        # TODO 重新加载图片的时间和地点信息
        for pic in self.pic_list:
            self.showPic(pic)

    def showPic(self, pic):
        self.hintFrame.hide()

        if self.sort_type == 1:
            sort_name = pic.location_str
        else:
            # TODO 时间还要排序一下
            sort_name = pic.time

        has_sort_list = False
        sort_item = None
        for s in self.sort_item_list:
            if s.sortLabel.text() == sort_name:
                has_sort_list = True
                sort_item = s
                break

        if has_sort_list:
            sort_item.addPicture(pic.url)
        else:
            s = SortListItem(self, sort_name)
            s.addPicture(pic.url)
            self.sort_item_list.append(s)
            self.formLayout.addWidget(s)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
