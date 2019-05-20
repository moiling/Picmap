#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 20:51
# @Author  : moiling
# @File    : apiRequest.py
import json
import urllib.request

import converter
from const import api


def find_route(way, origin, destination):
    req = urllib.request.urlopen(api.get_route_url(way, origin, destination))
    return converter.parse_api_route(req.read().decode())


def route_polyline(origin, destination):
    req = urllib.request.urlopen(api.get_route_url(api.WALKING, origin, destination))
    result = []
    info = req.read().decode()
    info = json.loads(info)
    path = info['route']['paths']
    for p in path:
        steps = p['steps']
        for s in steps:
            polyline = s['polyline'].split(';')
            for pl in polyline:
                result.append(pl)

    return result


def re_geocode(longitude, latitude):
    req = urllib.request.urlopen(api.get_geocode_url(str(longitude) + ',' + str(latitude)))
    return converter.parse_api_geocode(req.read().decode())
