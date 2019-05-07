#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 21:35
# @Author  : moiling
# @File    : testExifLocation.py
from libPicmap.exif import Exif

jpgWithLocation = '/Users/moi/Downloads/1.jpg'
jpgWithoutLocation = '/Users/moi/Downloads/2.jpg'
notJpg = '/Users/moi/Downloads/test.mov'

if __name__ == '__main__':
    # 以下操作全都没有判断错误信息，默认全是通过的，正常情况下要判断错误信息
    # 判断操作如 testExifError.py 中所示

    print('-----测试获取有Location图片-----')
    print(Exif(jpgWithLocation).location())

    print('-----测试获取无Location图片-----')
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.location())
    print(noLocation.error_info)

    print('--------测试非JPEG--------')
    noJpeg = Exif(notJpg)
    print(noJpeg.error_info)

    print('-----测试转移Location(只内存保存)--------')
    Exif(jpgWithLocation).transplant_location(noLocation)
    print(noLocation.location())
    # 重新读一次
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.location())

    print('-----测试转移Location(只外存保存)--------')
    Exif(jpgWithLocation).save_location_to(noLocation.url)
    print(noLocation.location())
    # 重新读一次
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.location())

    print('-----测试设置Location(只内存保存)--------')
    noLocation.set_location('113.405411,23.048562')
    print(noLocation.location())
    print('-----保存在外存--------')
    noLocation.save()
    # 重新读一次
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.location())

    print('-----测试只将Location改动保存在外存--------')
    noLocation.set_location('23.048562,113.405411')
    # 对comment也做一些改动
    noLocation.set_comment('yes')
    print(noLocation.location())
    print(noLocation.comment())
    noLocation.save_location()
    # 重新读一次
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.location())
    print(noLocation.comment())

    print('-----测试删除Location(只内存保存)--------')
    noLocation.remove_location()
    print(noLocation.location())
    print('-----保存在外存--------')
    noLocation.save()
    # 重新读一次
    noLocation = Exif(jpgWithoutLocation)
    print(noLocation.location())
