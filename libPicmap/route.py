#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 20:19
# @Author  : moiling
# @File    : route.py

import apiRequest
import converter
from carnival import Carnival
from const import api
import numpy as np

from exif import Exif


def programming_by_pic_start(pic_urls, start_info=(None, 0, 0, 0), way=api.WALKING):
    """
    :param pic_urls:
    :param start_info: 形如'x,y',100,100,200
    :param way:
    :return:
    """
    times = []
    locations = []
    if len(start_info) == 5:
        start_location = converter.location2str((start_info[0], start_info[1]))
        times.append((start_info[2], start_info[3], start_info[4]))
    else:
        start_location = start_info[0]
        times.append((start_info[1], start_info[2], start_info[3]))

    for pic in pic_urls:
        e = Exif(pic)
        time = e.pic_time()
        if not e.succeed:
            return False, e.error_info, 0, 0, 0

        location = e.location()
        if not e.succeed:
            return False, e.error_info, 0, 0, 0

        times.append(time)
        locations.append(location)

    return programming(times, locations, start_location, way)


def programming_by_all_pic(pic_urls, way=api.WALKING):
    n = len(pic_urls)
    times = []
    locations = []
    for i in range(n):
        e = Exif(pic_urls[i])
        time = e.pic_time()
        if not e.succeed:
            return False, e.error_info, 0, 0, 0

        location = e.location()
        if not e.succeed:
            return False, e.error_info, 0, 0, 0

        times.append(time)
        locations.append(location)

    start_location = locations[0]
    locations.remove(locations[0])

    return programming(times, locations, start_location, way)


def programming_by_infos(infos, way=api.WALKING):
    infos = np.array(infos)
    locations = list(infos[:, 0])
    start_location = locations[0]
    locations.remove(locations[0])
    times = list(infos[:, 1:])
    return programming(times, locations, start_location, way)


def programming(times, locations, start_location=None, way=api.WALKING):
    """
    :param way: 方式
    :param times: 所有的时间，(start_time, stay_time, end_time)元组，包括了开始点
    :param locations: 是形如 'x,y' 的字符串，或者(x,y)自动转
    :param start_location:
    :return:
        ok
        result_wrapper
        all_use_time
        all_wait_time
        all_walk_time
    """
    with_start = False if start_location is None else True

    n = len(times)
    t = [[0 for i in range(n)] for i in range(n)]

    for i in range(n - 1):
        for j in range(i + 1, n - 1):
            position_i = converter.location2str(locations[i])
            position_j = converter.location2str(locations[j])
            duration = apiRequest.find_route(way, position_i, position_j)
            t[i + 1][j + 1] = duration
            t[j + 1][i + 1] = duration

    if with_start:
        for i in range(n - 1):
            position_i = converter.location2str(locations[i])
            position_j = converter.location2str(start_location)
            duration = apiRequest.find_route(way, position_i, position_j)
            t[0][i + 1] = duration
            t[i + 1][0] = duration

    print(t)

    stt = []
    sty = []
    end = []
    for i in range(len(times)):
        stt.append(times[i][0])
        sty.append(times[i][1])
        end.append(times[i][2])

    c = Carnival(t, stt, sty, end)
    o, r = c.programming()
    if o:
        return o, wrapper_location_info(with_start, locations, start_location, c.wrapper_result(r, with_start)), \
               c.all_use_time(r, with_start), c.all_wait_time(r), c.all_walk_time(r)
    else:
        return o, r, 0, 0, 0


def wrapper_location_info(with_start, locations, start_location, wrapper):
    for i in range(len(locations) + (1 if with_start else 0)):
        if wrapper[i]['position'] == 0:
            wrapper[i]['location'] = converter.str2location(start_location)
        else:
            # 这个position如果在有start的时候就是对的，没有的时候会+1，所以要-1
            wrapper[i]['location'] = converter.str2location(locations[wrapper[i]['position'] - 1])

    return wrapper
