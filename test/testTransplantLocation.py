#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 23:11
# @Author  : moiling
# @File    : testTransplantLocation.py
from model import exif

jpgWithLocation = '/Users/moi/Documents/moi/mates/4E0D8F8BE8F58FD3720160D156D970FA.jpg'
jpgWithoutLocation = '/Users/moi/Downloads/57694370_p0.jpg'

if __name__ == '__main__':
    success, info = exif.transplant_location(jpgWithLocation, jpgWithoutLocation)
    print(info)
