#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 18:22
# @Author  : moiling
# @File    : testExifOther.py
from libPicmap.exif import Exif

jpgWithLocation = '/Users/moi/Downloads/1.jpg'
jpgWithoutLocation = '/Users/moi/Downloads/2.jpg'

if __name__ == '__main__':
    # 测试一些其他的Exif功能
    print('-----获取exif信息-----')
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.exif)

    print('-----获取url信息-----')
    print(noLocation.url)

    print('-----测试删除所有exif(仅内存)-----')
    noLocation.remove_all()
    print(noLocation.exif)
    # 再读一遍
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.exif)

    print('-----测试静态的删除所有exif方法，直接在外存操作-----')
    Exif.remove_all_and_save(jpgWithoutLocation)
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.exif)

    print('-----测试静态的移植exif方法，直接在外存操作-----')
    Exif.transplant(jpgWithLocation, jpgWithoutLocation)
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.exif)
