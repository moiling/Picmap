#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 19:54
# @Author  : moiling
# @File    : clone.py


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

    words = '%s -> %s' % (args.input, args.output)
    print(words)
