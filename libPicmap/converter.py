#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 19:06
# @Author  : moiling
# @File    : converter.py


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


def parse_pic_time(info):
    """
    解析exif comment中的时间格式
    :param info:
    :return:
        0th: start time
        1th: stay time
        2th: end time
    """
    # 如果格式不对的话，就返回默认的0 0 1440，1440表示24小时
    if not check_pic_time(info):
        return 0, 0, 1440

    num = info[3:-1].split(',')
    return int(num[0]), int(num[1]), int(num[2])


def rebuild_pic_time_by_str(start_time, stay_time, end_time):
    """
    :param start_time: 格式 x:xx 或 xx:xx 8:00 18:00
    :param stay_time: 格式 x:xx 1:32=>1小时32分钟 xx 32=>32分钟
    :param end_time: 格式 x:xx 或 xx:xx 8:00 18:00
    :return:
    """
    start_time = start_time.split(':')
    start_time = int(start_time[0]) * 60 + int(start_time[1])
    stay_time = stay_time.split(':')
    if len(stay_time) == 2:
        stay_time = int(stay_time[0]) * 60 + int(stay_time[1])
    else:
        stay_time = int(stay_time[0])
    end_time = end_time.split(':')
    end_time = int(end_time[0]) * 60 + int(end_time[1])
    return rebuild_pic_time(start_time, stay_time, end_time)


def rebuild_pic_time(start_time, stay_time, end_time):
    result = '@T('
    result += str(start_time)
    result += ','
    result += str(stay_time)
    result += ','
    result += str(end_time)
    result += ')'
    return result


def check_pic_time(info) -> bool:
    """
    @T(300,400,500)
    检查是否合法
    """
    # 结构合法
    if type(info) == str and len(info) >= 9 and info[:3] == '@T(' and info[-1] == ')':
        num_str = info[3:-1]
        num = num_str.split(',')
        # 数字必须3个，都得大于等于0，第3个要不能比第1个小，第2个不能超过3-2
        if len(num) == 3:
            try:
                num = (int(num[0]), int(num[1]), int(num[2]))
            except ValueError:
                return False

            if num >= (0, 0, 0) and num[2] - num[0] >= num[1]:
                return True

    return False
