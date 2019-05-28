#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 20:29
# @Author  : moiling
# @File    : show.py
from libPicmap.exif import Exif


def init(parser):
    parser.add_argument(
        'input',
        help='input picture url',
    )


def parse(args):
    e = Exif(args.input)
    longitude, latitude = e.location()
    if e.succeed:
        print('Location is {},{}'.format(longitude, latitude))
    else:
        print('Error: ' + e.error_info)

