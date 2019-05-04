#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-04 15:30
# @Author  : moiling
# @File    : testCarnivalProgramming.py
import json

from model.carnivalProgramming import Carnival


def test_programming():
    #   door    A       B       C       D       E
    t = [[0,    20,     40,     40,     140,    80],  # door
         [20,   0,      20,     20,     120,    60],  # A
         [40,   20,     0,      10,     60,     50],  # B
         [40,   20,     10,     0,      60,     40],  # C
         [140,  120,    60,     60,     0,      20],  # D
         [80,   60,     50,     40,     20,     0]]  # E
    stt = [460, 480,    1020,   1200,   600,    600]
    end = [460, 600,    1140,   1260,   720,    900]
    sty = [0,   60,     60,     60,     60,     60]

    '''
        # conflict test
        #   door     A       B       C       D       E
        t = [[0,     40,     40,     40,     140,    80],  # door
             [40,    0,      20,     20,     120,    60],  # A
             [40,    20,     0,      10,     60,     50],  # B
             [40,    20,     10,     0,      60,     40],  # C
             [140,   120,    60,     60,     0,      20],  # D
             [80,    60,     50,     40,     20,     0]]   # E
        stt = [460,  480,    1020,   1200,   600,    600]
        end = [460,  600,    1140,   1260,   720,    900]
        sty = [0,    60,     60,     60,     60,     60]
    '''

    '''
    #   door     1       2       3       4       5
    t = [[0,     60,     180,    120,    180,    180],  # door
         [60,    0,      120,    60,     120,    120],  # 1
         [180,   120,    0,      60,     120,    60],   # 2
         [120,   60,     60,     0,      60,     60],   # 3
         [180,   120,    120,    60,     0,      120],  # 4
         [180,   120,    60,     60,     120,    0]]    # 5
    stt = [420,  480,    540,    720,    1020,   480]
    end = [420,  1080,   1080,   840,    1200,   720]
    sty = [0,    60,     60,     60,     60,     60]
    '''

    c = Carnival(t, stt, sty, end)
    o, r = c.programming()
    if o:
        json_str = json.dumps(c.wrapper_result(r), indent=1)
        print('Succeed', json_str)
    else:
        print('Failed', r)


def test_programming_without_start():
    #   door     1       2       3       4       5
    t = [[0,     60,     180,    120,    180,    180],  # door
         [60,    0,      120,    60,     120,    120],  # 1
         [180,   120,    0,      60,     120,    60],   # 2
         [120,   60,     60,     0,      60,     60],   # 3
         [180,   120,    120,    60,     0,      120],  # 4
         [180,   120,    60,     60,     120,    0]]    # 5
    stt = [420,  480,    540,    720,    1020,   480]
    end = [420,  1080,   1080,   840,    1200,   720]
    sty = [0,    60,     60,     60,     60,     60]

    c = Carnival(t, stt, sty, end)
    o, r = c.programming_without_start()
    if o:
        json_str = json.dumps(c.wrapper_result(r), indent=1)
        print('Succeed', json_str)
    else:
        print('Failed', r)


if __name__ == '__main__':
    test_programming_without_start()
