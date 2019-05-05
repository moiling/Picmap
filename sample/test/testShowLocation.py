#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 21:35
# @Author  : moiling
# @File    : testShowLocation.py
from libPicmap import exif

jpgWithLocation = '/Users/moi/Documents/moi/mates/4E0D8F8BE8F58FD3720160D156D970FA.jpg'
jpgWithoutLocation = '/Users/moi/Documents/moi/mates/2FB422E23FD5039DB951D86B5B2C2DA5.jpg'
notJpg = '/Users/moi/Downloads/test.mov'

if __name__ == '__main__':
    success, r1, r2 = exif.pic2location(jpgWithLocation)
    if success:
        print(r1, ',', r2)
    else:
        print(r1)
