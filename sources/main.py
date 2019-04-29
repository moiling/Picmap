import sys

import piexif
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtGui

from sources.ui.mainWindow import Ui_MainWindow


class MainWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, evn):
        evn.accept()

    def dropEvent(self, evn: QtGui.QDropEvent):
        img_url = evn.mimeData().text()[7:]

        # 显示图片
        pixmap = QPixmap(img_url)
        pixmap = pixmap.scaled(200, 300)
        self.imgLabel.setPixmap(pixmap)

        # 读Exif信息
        exif_dict = piexif.load(img_url)

        # 显示所有Exif信息
        show_str = ""
        for ifd in ("0th", "Exif", "GPS", "1st"):
            for tag in exif_dict[ifd]:
                show_str += piexif.TAGS[ifd][tag]["name"] + str(exif_dict[ifd][tag]) + "\n"
        self.textLabel.setText(show_str)

        # 转换经纬度为经纬坐标，["GPS"][4]为经度元组，["GPS"][2]为维度元组，在_exif.py中有标明，按住ctrl点进piexif.TAGS可以进去看
        longitude = self.parse_location(exif_dict["GPS"][4])
        latitude = self.parse_location(exif_dict["GPS"][2])

        # 调用高德地图API，将地图网页显示在web engine view上
        dest_name = "照片拍摄地点"
        amap_key = "ebe67df3d77515f8b6269e8671616c78"

        self.webEngineView.load(QUrl("https://m.amap.com/navi/?dest=%lf,%lf&destName=%s&hideRouteIcon=1&key=%s" %
                                     (longitude, latitude, dest_name, amap_key)))

    @staticmethod
    def parse_location(info) -> float:
        return (info[0][0]) / (info[0][1]) + (info[1][0]) / (info[1][1]) / 60 + (info[2][0]) / (info[2][1]) / 3600


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = MainWindow()
    test.show()
    sys.exit(app.exec_())
