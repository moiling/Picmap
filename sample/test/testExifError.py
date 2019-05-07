#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 18:00
# @Author  : moiling
# @File    : testExifError.py
from libPicmap.exif import Exif

jpgWithLocation = '/Users/moi/Downloads/1.jpg'
jpgWithoutLocation = '/Users/moi/Downloads/2.jpg'
notJpg = '/Users/moi/Downloads/test.mov'

if __name__ == '__main__':
    # 所有的操作都是这样判断是否执行成功和报错的
    # 每次执行完一个方法都会修改Exif对象中的succeed值和error_info
    # error_info会保存上一个错误的信息，并不会因为成功而清空

    e = Exif(notJpg)
    if not e.succeed:
        print(e.error_info)

    e = Exif(jpgWithoutLocation)
    e.location()
    if not e.succeed:
        print(e.error_info)
