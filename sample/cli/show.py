#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 20:29
# @Author  : moiling
# @File    : show.py

from libPicmap import exif


def init(parser):
    parser.add_argument(
        'input',
        help='input picture url',
    )


def parse(args):
    success, longitude, latitude = exif.pic2location(args.input)
    if success:
        print('Location is {},{}'.format(longitude, latitude))
    else:
        print('Error: ' + longitude)

