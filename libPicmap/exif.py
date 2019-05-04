#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 20:48
# @Author  : moiling
# @File    : exif.py
import piexif
from PIL import Image


def pic2location(url):
    """
    :param url: picture url
    :return:
        0th: read exif succeed
        1th: if read succeed, return longitude, else return error information
        2th: if read succeed, return latitude, else None
    """
    succeed, data = pic2exif(url)
    if not succeed:
        return False, data, None

    return get_location_from_exif(data)


def get_location_from_exif(exif):
    # 检查是否有location信息
    if exif["GPS"] == {}:
        return False, 'no location information in exif', None

    # 转换经纬度为经纬坐标，["GPS"][4]为经度元组，["GPS"][2]为维度元组，在_exif.py中有标明，按住ctrl点进piexif.TAGS可以进去看
    longitude = parse_location(exif["GPS"][4])
    latitude = parse_location(exif["GPS"][2])

    return True, longitude, latitude


def pic2exif(url):
    """
    :param url: picture url
    :return:
        0th: read exif succeed
        1th: if read succeed, return exif dict, else return error information
    """
    # 检查是否是jpeg
    if not is_jpeg(url):
        return False, 'not a jpeg'

    # 读Exif信息
    exif_dict = piexif.load(url)

    if exif_dict is not None:
        return True, exif_dict
    else:
        return False, 'exif is none'


def exif2str(exif):
    show_str = ""
    for ifd in ("0th", "Exif", "GPS", "1st"):
        for tag in exif[ifd]:
            show_str += piexif.TAGS[ifd][tag]["name"] + str(exif[ifd][tag]) + "\n"
    return show_str


def transplant_all_exif(input_url, output_url):
    # 检查是否是jpeg
    if not is_jpeg(input_url):
        return False, input_url + 'is not a jpeg'
    if not is_jpeg(output_url):
        return False, output_url + 'is not a jpeg'

    piexif.transplant(input_url, output_url)
    return True, 'succeed'


def remove_all_exif(url):
    piexif.remove(url)


def remove_location(url):
    success, data = pic2exif(url)
    if not success:
        return False, data

    data['GPS'] = {}
    piexif.insert(piexif.dump(data), url)
    return True, 'succeed'


def insert_location(url, location):
    longitude_str, latitude_str = location.split(',')
    longitude = float(longitude_str)
    latitude = float(latitude_str)
    return insert_longitude_latitude(url, longitude, latitude)


def insert_longitude_latitude(url, longitude, latitude):
    success, data = pic2exif(url)
    if not success:
        return False, data
    data["GPS"][4] = rebuild_location(longitude)
    data["GPS"][2] = rebuild_location(latitude)

    piexif.insert(piexif.dump(data), url)
    return True, 'succeed'


def transplant_location(input_url, output_url):
    success, data_in = pic2exif(input_url)
    if not success:
        return False, data_in
    success, data_out = pic2exif(output_url)
    if not success:
        return False, data_out

    if data_in["GPS"] == {}:
        return False, input_url + 'is no location information in exif'

    data_out["GPS"] = data_in['GPS']

    piexif.insert(piexif.dump(data_out), output_url)
    return True, 'succeed'


def is_jpeg(url) -> bool:
    try:
        i = Image.open(url)
        return i.format == 'JPEG'
    except IOError:
        return False


def parse_location(info) -> float:
    """
    将exif中时分秒的地址格式转换为小数格式
    :param info: 单独的longitude或latitude时分秒格式（元组）
    :return: 转换后的小数格式（float）
    """
    return (info[0][0]) / (info[0][1]) + (info[1][0]) / (info[1][1]) / 60 + (info[2][0]) / (info[2][1]) / 3600


def rebuild_location(info):
    """
    将小数位的location信息重新转化成exif所需的时分秒格式
    :param info: 单独的longitude或latitude的小数格式（float）
    :return: 转换后的时分秒格式（元组）
    """
    hours = int(info)
    minutes = int((info - hours) * 60)
    seconds = int(((info - hours) * 60 - minutes) * 60 * 10000)
    result = ((hours, 1), (minutes, 1), (seconds, 10000))
    return result
