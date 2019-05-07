#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 22:51
# @Author  : moiling
# @File    : api.py

web_serve_key = 'c35692f8b41d4c3444ad3a321e4fe474'
js_api_key = '63902cd084cbbafc4bcfaf0d7abc06c7'
url_api_key = 'ebe67df3d77515f8b6269e8671616c78'

WALKING = 'walking'
TRANSIT = 'transit'
DRIVING = 'driving'
BICYCLING = 'bicycling'
TRUCK = 'truck'

route_url = 'https://restapi.amap.com/v3/direction/{}?origin={}&destination={}&key={}'


def get_route_url(route_way, origin, destination, key=web_serve_key):
    return route_url.format(route_way, origin, destination, key)
