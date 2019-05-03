#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 19:38
# @Author  : moiling
# @File    : picmap.py

import argparse
from cli import *


def _init_subparsers(parent):
    subparsers = parent.add_subparsers(
        title='sub commands',
        description='valid subcommands',
        help='config subscommand help'
    )

    parser_clone = subparsers.add_parser(
        'clone',
        help='Clone a picture\'s exif information into a new picture'
    )

    clone.init(parser_clone)
    parser_clone.set_defaults(func=clone.parse)

    parser_show = subparsers.add_parser(
        'show',
        help='Show a picture\'s exif information'
    )

    show.init(parser_show)
    parser_show.set_defaults(func=show.parse)


def _parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-v', '--version',
        action='version',
        version='%(prog)s 1.0.0',
    )

    _init_subparsers(parser)

    return parser.parse_args()


if __name__ == '__main__':
    args = _parse_args()
    args.func(args)
