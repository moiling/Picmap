import os

from PyQt5.QtCore import *
import sys

from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QApplication, QMainWindow

from test.source.ui.jsApiTestWindow import Ui_TestWindow

app, browser = None, None


class TestCallback(QObject):

    @pyqtSlot(str, result=str)
    def js_callback(self, location):
        print("js_callback:" + location)
        return location


class TestWindow(Ui_TestWindow, QMainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

        self.channel = QWebChannel()  # 增加一个通信中需要用到的频道
        self.test_callback = TestCallback()
        self.channel.registerObject('test_callback', self.test_callback)  # 将功能类注册到频道中，注册名可以任意，但将在网页中作为标识
        self.webEngineView.page().setWebChannel(self.channel)  # 在浏览器中设置该频道

        # 加载js
        self.webEngineView.setHtml(open(os.path.dirname(os.path.dirname(__file__)) + '/resource/web/jsApiTest.html')
                                   .read())

        self.pushButton.clicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        # py动态调用js
        print("button click")
        js_string = '''
            var marker = new AMap.Marker({
                position:[116.39, 39.9]//位置
            })
            map.add(marker);//添加到地图
        '''
        self.webEngineView.page().runJavaScript(js_string)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = TestWindow()
    test.show()
    sys.exit(app.exec_())
