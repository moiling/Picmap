#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-04 00:29
# @Author  : moiling
# @File    : clear.py
from exif import Exif


def init(parser):
    parser.add_argument(
        'input',
        help='input picture url',
    )


def parse(args):
    e = Exif(args.input)
    e.remove_location()
    if e.succeed:
        print(e.succeed)
    else:
        print(e.error_info)
