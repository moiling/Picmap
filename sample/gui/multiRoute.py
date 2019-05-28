#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 07:15
# @Author  : moiling
# @File    : multiRoute.py

# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 01:43
# @Author  : moiling
# @File    : pictureDetail.py

import os
import sys

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from libPicmap import apiRequest
from libPicmap import route
from libPicmap.exif import Exif
from sample.gui.ui.multiRouteWindow import Ui_MainWindow


class Callback(QObject):

    def __init__(self, window):
        super().__init__()
        self.window = window

    @pyqtSlot(str, result=str)
    def js_callback(self, location):
        if self.window.is_set_start:
            try:
                self.window.okButton.clicked.disconnect()
            except TypeError:
                pass
            self.window.hintLabel.setText('确定选择该点？')
            self.window.okButton.show()
            self.window.okButton.clicked.connect(lambda: self.window.select_start_location(location))


class MultiRouteWindow(Ui_MainWindow, QMainWindow):
    is_set_start = False
    start_location = None
    is_select_pic = False
    is_route = True

    def __init__(self, urls):
        super().__init__()
        self.setupUi(self)
        self.urls = urls
        self.hintFrame.hide()

        self.channel = QWebChannel()  # 增加一个通信中需要用到的频道
        self.callback = Callback(self)
        self.channel.registerObject('callback', self.callback)  # 将功能类注册到频道中，注册名可以任意，但将在网页中作为标识

        # for py installer
        if getattr(sys, 'frozen', False):
            self.root_path = os.path.dirname(sys.executable)
        elif __file__:
            self.root_path = os.path.dirname(__file__)
        else:
            self.root_path = '.'

        self.loadHtml()

        self.startTimeEdit.setText(str(0))
        self.routeButton.setEnabled(False)

        self.selectStartFromMap.clicked.connect(self.on_select_from_map_click)
        self.selectStartPic.clicked.connect(self.on_select_start_pic_click)
        self.routeButton.clicked.connect(self.route)
        self.cancelButton.clicked.connect(self.back)

    def loadHtml(self):
        self.webEngineView.page().setWebChannel(self.channel)  # 在浏览器中设置该频道

        # 加载js
        self.webEngineView.setHtml(
            open(self.root_path + '/resource/web/multiRoute.html', encoding='utf-8').read())

        self.webEngineView.page().loadFinished.connect(self.show_location)

    @pyqtSlot()
    def route(self):
        self.is_route = True
        self.optionFrame.hide()
        self.okButton.hide()
        self.hintFrame.show()

        if self.is_select_pic:
            o, r, use, wait, walk = route.programming_by_all_pic(
                self.urls
            )
            if not o:
                QMessageBox.warning(self, "错误", r, QMessageBox.Yes, QMessageBox.Yes)
                return
        else:
            if self.start_location is not None:
                o, r, use, wait, walk = route.programming_by_pic_start(
                    self.urls,
                    (self.start_location, int(self.startTimeEdit.text()), 0, int(self.startTimeEdit.text())),
                )
                if not o:
                    QMessageBox.warning(self, "错误", r, QMessageBox.Yes, QMessageBox.Yes)
                    return
            else:
                QMessageBox.warning(self, "错误", '未设置出发点', QMessageBox.Yes, QMessageBox.Yes)
                return

        self.hintLabel.setText('总耗时：' + str(use) + '分钟，总等待时间：' + str(wait) + '分钟，总路程时间：' + str(walk) + '分钟')

        js_string = '''
            map.clearMap();
        '''
        self.webEngineView.page().runJavaScript(js_string)

        for i in range(len(r) - 1):

            polyline = apiRequest.route_polyline(str(r[i]['location'][0]) + ',' + str(r[i]['location'][1]),
                                                 str(r[i + 1]['location'][0]) + ',' + str(r[i + 1]['location'][1]))
            js_string = '''
                var path = [
            '''
            for location in polyline:
                js_string += '''
                    new AMap.LngLat(''' + location + '''),
                '''
            js_string += '''
                ];
                // 创建折线实例
                var polyline = new AMap.Polyline({
                    path: path,  
                    borderWeight: 2, // 线条宽度，默认为 1
                    strokeColor: ''' + ('\'red\'' if (i % 2 == 0) else '\'blue\'') + ''', // 线条颜色
                    lineJoin: 'round' // 折线拐点连接处样式
                });
                
                // 将折线添加至地图实例
                map.add(polyline);
                
                var marker = new AMap.Marker({
                    position:[''' + str(r[i]['location'][0]) + ',' + str(r[i]['location'][1]) + ''']//位置
                })
                marker.setLabel({
                    offset: new AMap.Pixel(0, 0),  //设置文本标注偏移量
                    content: "<div class='info'>''' + str(i) + '''</div>", //设置文本标注内容
                });
                map.add(marker);//添加到地图
                
                var marker = new AMap.Marker({
                    position:[''' + str(r[i + 1]['location'][0]) + ',' + str(r[i + 1]['location'][1]) + ''']//位置
                })
                marker.setLabel({
                    offset: new AMap.Pixel(0, 0),  //设置文本标注偏移量
                    content: "<div class='info'>''' + str(i + 1) + '''</div>", //设置文本标注内容
                });
                map.add(marker);//添加到地图
                
            '''

            self.webEngineView.page().runJavaScript(js_string)

    @pyqtSlot()
    def on_select_start_pic_click(self):
        self.routeButton.setEnabled(True)
        self.is_select_pic = True
        self.startTimeEdit.setText(str(Exif(self.urls[0]).pic_time()[0]))
        self.startTimeEdit.setEnabled(False)

    @pyqtSlot()
    def select_start_location(self, location):
        self.routeButton.setEnabled(True)
        self.start_location = location
        self.startInfoLabel.setText('已从地图中选择出发点')
        self.is_set_start = False
        self.hintFrame.hide()
        self.optionFrame.show()

    @pyqtSlot()
    def show_location(self):
        for url in self.urls:
            # 读Exif信息
            exif = Exif(url)

            if not exif.succeed:
                QMessageBox.warning(self, "错误", exif.error_info, QMessageBox.Yes, QMessageBox.Yes)
                return

            longitude, latitude = exif.location()

            if not exif.succeed:
                QMessageBox.warning(self, "错误", exif.error_info, QMessageBox.Yes, QMessageBox.Yes)
                return

            js_string = '''
                var marker = new AMap.Marker({
                    position:[''' + str(longitude) + ',' + str(latitude) + ''']//位置
                })
                map.add(marker);//添加到地图
                map.setCenter([''' + str(longitude) + ',' + str(latitude) + '''])
            '''
            self.webEngineView.page().runJavaScript(js_string)

    def back(self):
        self.hintFrame.hide()
        self.optionFrame.show()

        if self.is_route:
            self.loadHtml()
            self.show_location()

        self.is_route = False
        self.is_set_start = False

    @pyqtSlot()
    def on_select_from_map_click(self):
        self.startTimeEdit.setEnabled(True)
        self.is_select_pic = False
        self.is_set_start = True

        self.optionFrame.hide()
        self.hintLabel.setText("请在地图上点击选择出发点")
        self.okButton.hide()
        self.hintFrame.show()
