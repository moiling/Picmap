#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 19:54
# @Author  : moiling
# @File    : clone.py
from exif import Exif


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
    print(Exif.transplant(args.input, args.output))
