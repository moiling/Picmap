#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 01:43
# @Author  : moiling
# @File    : pictureDetail.py
import os

from PyQt5 import QtGui, Qt
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QDialog

from exif import Exif
from gui.ui.pictureDetailWindow import Ui_MainWindow


class Callback(QObject):

    def __init__(self, window):
        super().__init__()
        self.window = window

    @pyqtSlot(str, result=str)
    def js_callback(self, location):
        print("js_callback:" + location)
        if self.window.is_set_start:
            # TODO 添加提示Dialog，如果点了确定才继续执行
            self.window.is_set_start = False
            self.window.go(location)


class PictureDetailWindow(Ui_MainWindow, QMainWindow):

    closed = pyqtSignal()
    is_set_start = False

    def __init__(self, url):
        super().__init__()
        self.setupUi(self)

        # 读Exif信息
        e = Exif(url)

        if not e.succeed:
            # TODO 显示失败原因在界面上
            return

        self.longitude, self.latitude = e.location()

        if not e.succeed:
            # TODO 显示失败原因在界面上
            return

        self.channel = QWebChannel()  # 增加一个通信中需要用到的频道
        self.callback = Callback(self)
        self.channel.registerObject('callback', self.callback)  # 将功能类注册到频道中，注册名可以任意，但将在网页中作为标识
        self.webEngineView.page().setWebChannel(self.channel)  # 在浏览器中设置该频道

        # 加载js
        self.webEngineView.setHtml(open(os.path.dirname(__file__) + '/resource/web/pictureDetail.html', encoding='utf-8')
                                   .read())

        self.webEngineView.page().loadFinished.connect(self.show_location)

        self.goButton.clicked.connect(self.on_go_click)

    def show_location(self):
        js_string = '''
            var marker = new AMap.Marker({
                position:[''' + str(self.longitude) + ',' + str(self.latitude) + ''']//位置
            })
            map.add(marker);//添加到地图
            map.setCenter([''' + str(self.longitude) + ',' + str(self.latitude) + '''])
        '''
        self.webEngineView.page().runJavaScript(js_string)

    def on_go_click(self):
        # TODO 添加提示Dialog
        self.is_set_start = True

    def go(self, start_location):
        # TODO 还要选择行走方式
        js_string = '''
            AMap.plugin('AMap.Driving', function() {
              var driving = new AMap.Driving({
                policy: AMap.DrivingPolicy.LEAST_TIME,
                map: map,
                panel: 'panel'
              })
              
              var startLngLat = [''' + start_location + ''']
              var endLngLat = [''' + str(self.longitude) + ',' + str(self.latitude) + ''']
              
              driving.search(startLngLat, endLngLat, function (status, result) {
                // 未出错时，result即是对应的路线规划方案
              })
            })
        '''
        self.webEngineView.page().runJavaScript(js_string)

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.closed.emit()
