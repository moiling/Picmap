#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-20 01:43
# @Author  : moiling
# @File    : pictureDetail.py
import os

from PyQt5 import QtGui
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox

from const import api
from exif import Exif
from gui.changeTimeDialog import ChangeTimeDialog
from gui.ui.pictureDetailWindow import Ui_MainWindow


class Callback(QObject):

    def __init__(self, window):
        super().__init__()
        self.window = window

    @pyqtSlot(str, result=str)
    def js_callback(self, location):
        if self.window.is_set_start:
            try:
                self.window.ok_clicked.disconnect()
            except TypeError:
                pass
            self.window.label.setText('确定选择该点？')
            self.window.okButton.show()
            self.window.ok_clicked.connect(lambda: self.window.go(location))

        if self.window.is_change_location:
            try:
                self.window.ok_clicked.disconnect()
            except TypeError:
                pass
            self.window.label.setText('确定选择该点？')
            self.window.okButton.show()
            self.window.ok_clicked.connect(lambda: self.window.change_location(location))


class PictureDetailWindow(Ui_MainWindow, QMainWindow):

    closed = pyqtSignal()
    ok_clicked = pyqtSignal()
    is_set_start = False
    is_change_location = False
    is_show_around = False

    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.hintFrame.hide()

        # 读Exif信息
        self.exif = Exif(url)

        if not self.exif.succeed:
            QMessageBox.warning(self, "错误", self.exif.error_info, QMessageBox.Yes, QMessageBox.Yes)
            return

        self.longitude, self.latitude = self.exif.location()

        if not self.exif.succeed:
            QMessageBox.warning(self, "错误", self.exif.error_info, QMessageBox.Yes, QMessageBox.Yes)
            return

        self.channel = QWebChannel()  # 增加一个通信中需要用到的频道
        self.callback = Callback(self)
        self.channel.registerObject('callback', self.callback)  # 将功能类注册到频道中，注册名可以任意，但将在网页中作为标识

        self.loadHtml()

        self.goButton.clicked.connect(self.on_go_click)
        self.locationButton.clicked.connect(self.on_location_click)
        self.backButton.clicked.connect(self.back)
        self.aroundButton.clicked.connect(self.show_around)
        self.okButton.clicked.connect(self.on_ok_click)
        self.timeButton.clicked.connect(self.on_time_click)

    @pyqtSlot()
    def on_time_click(self):
        dialog = ChangeTimeDialog(self.exif)
        rec = dialog.exec_()
        if rec == QDialog.Accepted:
            self.exif.set_pic_time(int(dialog.startTimeEdit.text()), int(dialog.stayTimeEdit.text()),
                                   int(dialog.endTimeEdit.text()))
            self.exif.save()

    @pyqtSlot()
    def on_ok_click(self):
        self.ok_clicked.emit()

    def loadHtml(self):
        self.webEngineView.page().setWebChannel(self.channel)  # 在浏览器中设置该频道

        # 加载js
        self.webEngineView.setHtml(
            open(os.path.dirname(__file__) + '/resource/web/pictureDetail.html', encoding='utf-8')
            .read())

        self.webEngineView.page().loadFinished.connect(self.show_location)

    @pyqtSlot()
    def show_around(self):
        self.webEngineView.load(QUrl(
            'https://m.amap.com/around/?locations={},{}&keywords=美食,KTV,地铁站,公交站&defaultIndex=3&defaultView=&searchRadius=5000&key={}'
                .format(self.longitude, self.latitude, api.url_api_key)))

        self.is_show_around = True

        self.optionFrame.hide()
        self.label.setText('')
        self.okButton.hide()
        self.hintFrame.show()

    def back(self):
        self.hintFrame.hide()
        self.optionFrame.show()

        if self.is_show_around:
            self.loadHtml()
            self.show_location()

        self.is_set_start = False
        self.is_change_location = False
        self.is_show_around = False

    @pyqtSlot()
    def show_location(self):
        js_string = '''
            map.clearMap();
            var marker = new AMap.Marker({
                position:[''' + str(self.longitude) + ',' + str(self.latitude) + ''']//位置
            })
            map.add(marker);//添加到地图
            map.setCenter([''' + str(self.longitude) + ',' + str(self.latitude) + '''])
        '''
        self.webEngineView.page().runJavaScript(js_string)

    @pyqtSlot()
    def on_go_click(self):
        self.is_set_start = True

        self.optionFrame.hide()
        self.label.setText("请在地图上点击选择出发点")
        self.okButton.hide()
        self.hintFrame.show()

    @pyqtSlot()
    def on_location_click(self):
        self.is_change_location = True

        self.optionFrame.hide()
        self.label.setText("请在地图上点击选择需要更改的地点")
        self.okButton.hide()
        self.hintFrame.show()

    def change_location(self, new_location):
        self.is_set_start = False

        self.longitude, self.latitude = new_location.split(',')
        self.exif.set_location(new_location)
        self.exif.save()
        # 刷新地图
        self.show_location()

        self.optionFrame.show()
        self.hintFrame.hide()

    def go(self, start_location):
        self.is_set_start = False
        # TODO 还要选择行走方式
        js_string = '''
            map.clearMap();
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

        self.optionFrame.show()
        self.hintFrame.hide()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.closed.emit()
