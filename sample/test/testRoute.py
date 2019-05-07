#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 20:22
# @Author  : moiling
# @File    : testRoute.py
import json

from libPicmap import route

start_pic_url = './pic/start.jpg'
a_pic_url = './pic/a.jpg'
b_pic_url = './pic/b.jpg'
c_pic_url = './pic/c.jpg'
d_pic_url = './pic/d.jpg'
e_pic_url = './pic/e.jpg'


def use_programming():
    """
    使用time信息和locations信息
    start_location单独提出来，其他导航的locations放在数组中
    time包含了start和其他的时间段，数组第一位为start的时间段
    start_location并不是必要参数，可以不用开始地点进行导航
    但是time必须要要有start，不然不知道什么时候开始
    所以time的数组大小=locations的数组大小+1，注意
    """
    a = '113.324153,23.127072'
    b = '113.340032,23.13461'
    c = '113.340289,23.114245'
    d = '113.402774,23.122218'
    e = '113.384492,23.118113'

    times = [(480, 0, 480),
             (480, 60, 600),
             (1020, 60, 1140),
             (1200, 60, 1300),
             (600, 60, 750),
             (600, 60, 900)]

    o, r, use, wait, walk = route.programming(times, (a, b, c, d, e))
    if o:
        json_str = json.dumps(r, indent=1)
        print('Succeed', json_str)
        print('all use time:', use)
        print('all wait time:', wait)
        print('all walk time:', walk)
    else:
        print('Failed', r)


def use_programming_by_infos():
    """
    使用地点信息数组
    格式为 'x,y',start_time,stay_time,end_time 或 x,y,start_time,stay_time,end_time
    """
    infos = [(None, 480, 0, 480),
             ('113.324153,23.127072', 480, 60, 600),
             ('113.340032,23.13461', 1020, 60, 1140),
             ('113.340289,23.114245', 1200, 60, 1300),
             ('113.402774,23.122218', 600, 60, 750),
             ('113.384492,23.118113', 600, 60, 900)]

    o, r, use, wait, walk = route.programming_by_infos(infos)
    if o:
        json_str = json.dumps(r, indent=1)
        print('Succeed', json_str)
        print('all use time:', use)
        print('all wait time:', wait)
        print('all walk time:', walk)
    else:
        print('Failed', r)


def use_programming_by_all_pic():
    """
    使用定义的全部地点图片
    图片全用url
    注意start必须放在第一个，第一个被识别为开始点，时间信息全在图片中
    """
    o, r, use, wait, walk = route.programming_by_all_pic(
        (start_pic_url, a_pic_url, b_pic_url, c_pic_url, d_pic_url, e_pic_url)
    )
    if o:
        json_str = json.dumps(r, indent=1)
        print('Succeed', json_str)
        print('all use time:', use)
        print('all wait time:', wait)
        print('all walk time:', walk)
    else:
        print('Failed', r)


def use_programming_by_pic_start():
    """
    使用定义的一个开始点和几张地点图片
    图片全用url
    开始点格式为 'x,y',start_time,stay_time,end_time 或 x,y,start_time,stay_time,end_time
    """
    o, r, use, wait, walk = route.programming_by_pic_start(
        (a_pic_url, b_pic_url, c_pic_url, d_pic_url, e_pic_url),
        ('113.324153,23.127072', 480, 0, 480),
    )
    if o:
        json_str = json.dumps(r, indent=1)
        print('Succeed', json_str)
        print('all use time:', use)
        print('all wait time:', wait)
        print('all walk time:', walk)
    else:
        print('Failed', r)


if __name__ == '__main__':
    # use_programming()
    # use_programming_by_infos()
    # use_programming_by_all_pic()
    use_programming_by_pic_start()
