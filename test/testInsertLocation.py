#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 23:18
# @Author  : moiling
# @File    : testInsertLocation.py
from libPicmap import exif

jpgWithoutLocation = '/Users/moi/Downloads/74499914_p0.jpg'
location = '113.405411,23.048562'

if __name__ == '__main__':
    success, info = exif.insert_location(jpgWithoutLocation, location)
    print(info)
