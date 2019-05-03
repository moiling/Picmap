#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 23:54
# @Author  : moiling
# @File    : testRemoveLocation.py
from model import exif

jpgWithLocation = '/Users/moi/Downloads/74499914_p0.jpg'

if __name__ == '__main__':
    success, info = exif.remove_location(jpgWithLocation)
    print(info)
