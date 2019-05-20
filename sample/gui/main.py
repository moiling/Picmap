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
from gui.multiRoute import MultiRouteWindow
from gui.sortListItem import SortListItem
from gui.ui.mainWindow import Ui_MainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui


class MainWindow(Ui_MainWindow, QMainWindow):

    pic_list = []
    select_pic_list = []
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
        self.multiRouteButton.clicked.connect(self.on_multi_route_clicked)

    def dragEnterEvent(self, evn):
        evn.accept()

    def dropEvent(self, evn: QtGui.QDropEvent):
        file_urls = evn.mimeData().text().split('\n')

        for file_url in file_urls:
            if file_url == '':
                return

            if file_url[:7] != 'file://':
                # TODO 显示失败原因在界面上
                return
            if file_url[9] == ':':
                # file:///C:,第9位是:的大概就是windows了
                img_url = file_url[8:]
            else:
                img_url = file_url[7:]

            pic = self.loadLocation(img_url)
            if not pic:
                continue

            self.pic_list.append(pic)
            self.showPic(pic)

    @staticmethod
    def loadLocation(url):

        # 读Exif信息
        e = Exif(url)

        if not e.succeed:
            # TODO 显示失败原因在界面上
            return False

        longitude, latitude = e.location()

        if not e.succeed:
            # TODO 显示失败原因在界面上
            return False

        # 转换成地点信息
        country, province, city = apiRequest.re_geocode(longitude, latitude)

        if type(city) is str:
            location_str = country + ' ' + province + ' ' + city
        else:
            location_str = country + ' ' + province

        pic = Pic(url, location_str, time.ctime(os.path.getctime(url)))
        return pic

    @pyqtSlot()
    def show_pic_details(self, url):
        self.detailWidget.show()
        self.nameText.setText(os.path.basename(os.path.realpath(url)))
        self.urlText.setText(url)

        pic = None
        for p in self.pic_list:
            if p.url == url:
                pic = p

        if pic is not None:
            self.locationText.setText(pic.location_str)
            self.timeText.setText(pic.time)

    @pyqtSlot()
    def select_pic(self, url, checked):
        if checked:
            self.select_pic_list.append(url)
        else:
            self.select_pic_list.remove(url)

        if len(self.select_pic_list) > 1:
            self.multiRouteButton.setEnabled(True)
        else:
            self.multiRouteButton.setEnabled(False)

    windowList = []
    @pyqtSlot()
    def on_multi_route_clicked(self):
        the_window = MultiRouteWindow(self.select_pic_list)
        self.windowList.append(the_window)
        the_window.show()

    @pyqtSlot()
    def hide_pic_details(self):
        self.detailWidget.hide()

    @pyqtSlot()
    def set_sort_type(self):
        self.sort_type = self.sortComboBox.currentIndex()
        self.sort()

    def sort(self):
        # 清空
        for s in self.sort_item_list:
            self.formLayout.removeWidget(s)
            s.deleteLater()

        self.sort_item_list.clear()

        for pic in self.pic_list:
            self.showPic(pic)

    def refresh(self, url):
        for p in self.pic_list:
            if p.url == url:
                self.pic_list.remove(p)
                break

        pic = self.loadLocation(url)
        self.pic_list.append(pic)

        self.sort()

        # 因为可能详细信息正好刷新了，还是隐藏为妙
        self.detailWidget.hide()

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
