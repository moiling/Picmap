#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-04 00:29
# @Author  : moiling
# @File    : clear.py
from libPicmap import exif


def init(parser):
    parser.add_argument(
        'input',
        help='input picture url',
    )


def parse(args):
    success, info = exif.remove_location(args.input)
    print(info)
