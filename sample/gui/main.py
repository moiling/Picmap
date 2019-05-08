import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui

from exif import Exif
from libPicmap.const import *
from gui.ui.mainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, evn):
        evn.accept()

    def dropEvent(self, evn: QtGui.QDropEvent):
        file_url = evn.mimeData().text()
        if file_url[:7] != 'file://':
            # TODO 显示失败原因在界面上
            return
        if file_url[9] == ':':
            # file:///C:,第9位是:的大概就是windows了
            img_url = evn.mimeData().text()[8:]
        else:
            img_url = evn.mimeData().text()[7:]

        # 显示图片
        pixmap = QPixmap(img_url)
        pixmap = pixmap.scaled(200, 300)
        self.imgLabel.setPixmap(pixmap)

        # 读Exif信息
        e = Exif(img_url)

        if not e.succeed:
            # TODO 显示失败原因在界面上
            return

        # 显示所有Exif信息
        self.textLabel.setText(e.__str__())

        longitude, latitude = e.location()

        if not e.succeed:
            # TODO 显示失败原因在界面上
            return

        # 调用高德地图API，将地图网页显示在web engine view上
        dest_name = "照片拍摄地点"
        self.webEngineView.load(QUrl("https://m.amap.com/navi/?dest=%lf,%lf&destName=%s&hideRouteIcon=1&key=%s" %
                                     (longitude, latitude, dest_name, api.url_api_key)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())
