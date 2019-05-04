#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 19:54
# @Author  : moiling
# @File    : clone.py
from libPicmap import exif


def init(parser):
    parser.add_argument(
        'input',
        help='input picture url',
    )
    parser.add_argument(
        'output',
        help='output picture url',
    )


def parse(args):
    success, info = exif.transplant_location(args.input, args.output)
    print(info)
