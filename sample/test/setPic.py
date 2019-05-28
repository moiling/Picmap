#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 23:04
# @Author  : moiling
# @File    : setPic.py
from libPicmap.exif import Exif

start_pic_url = './pic/start.jpg'
a_pic_url = './pic/a.jpg'
b_pic_url = './pic/b.jpg'
c_pic_url = './pic/c.jpg'
d_pic_url = './pic/d.jpg'
e_pic_url = './pic/e.jpg'

if __name__ == '__main__':
    """
    给测试用的图片添加地点和时间信息
    """
    start = Exif(start_pic_url)
    start.set_location('113.324153,23.127072')
    start.set_pic_time(480, 0, 480)
    start.save()

    a = Exif(a_pic_url)
    a.set_location('113.324153,23.127072')
    a.set_pic_time(480, 60, 600)
    a.save()

    b = Exif(b_pic_url)
    b.set_location('113.340032,23.13461')
    b.set_pic_time(1020, 60, 1140)
    b.save()

    c = Exif(c_pic_url)
    c.set_location('113.340289,23.114245')
    c.set_pic_time(1200, 60, 1300)
    c.save()

    d = Exif(d_pic_url)
    d.set_location('113.402774,23.122218')
    d.set_pic_time(600, 60, 750)
    d.save()

    e = Exif(e_pic_url)
    e.set_location('113.384492,23.118113')
    e.set_pic_time(600, 60, 900)
    e.save()

