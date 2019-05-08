#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-04 00:30
# @Author  : moiling
# @File    : add.py
from exif import Exif


def init(parser):
    parser.add_argument(
        'input',
        help='input picture url',
    )
    parser.add_argument(
        'longitude',
        help='longitude',
    )
    parser.add_argument(
        'latitude',
        help='latitude',
    )


def parse(args):
    e = Exif(args.input)
    e.set_longitude_latitude(float(args.longitude), float(args.latitude))
    if e.succeed:
        print(e.succeed)
    else:
        print(e.error_info)
