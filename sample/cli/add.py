#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-04 00:30
# @Author  : moiling
# @File    : add.py
from libPicmap import exif


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
    success, info = exif.insert_longitude_latitude(args.input, float(args.longitude), float(args.latitude))
    print(info)
