#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-03 20:48
# @Author  : moiling
# @File    : exif.py
import piexif
import piexif.helper
from PIL import Image

import converter


class Exif:

    def __init__(self, url):
        self.url = url
        self.exif = None
        self.error_info = None
        self.succeed = False

        self.__exif(url)

    def __exif(self, url):
        # 检查是否是jpeg
        if self.is_jpeg(url):
            # 读exif
            self.exif = piexif.load(url)
            self.has_info()

    def location(self):
        """
        :return:
            0th: longitude
            1th: latitude
        """
        # 检查是否有location信息
        if not self.has_gps_info():
            return None, None

        longitude = converter.parse_location(self.exif["GPS"][piexif.GPSIFD.GPSLongitude])
        latitude = converter.parse_location(self.exif["GPS"][piexif.GPSIFD.GPSLatitude])
        self.succeed = True
        return longitude, latitude

    def pic_time(self):
        comment = self.comment()
        if not self.succeed:
            return None, None, None

        return converter.parse_pic_time(comment)

    def comment(self):
        if not self.has_exif_info():
            return None

        try:
            user_comment = piexif.helper.UserComment.load(self.exif["Exif"][piexif.ExifIFD.UserComment])
        except KeyError:
            self.error_info = 'no user comment information'
            self.succeed = False
            return None

        if user_comment == '':
            self.error_info = 'no user comment information'
            self.succeed = False
            return None

        self.succeed = True
        return user_comment

    def __str__(self):
        show_str = ""
        for ifd in ("0th", "Exif", "GPS", "1st"):
            for tag in self.exif[ifd]:
                show_str += piexif.TAGS[ifd][tag]["name"] + str(self.exif[ifd][tag]) + "\n"
        self.succeed = True
        return show_str

    def save(self):
        return self.save_to(self.url)

    def save_to(self, url):
        if not self.is_jpeg(url):
            return False

        piexif.insert(piexif.dump(self.exif), url)
        self.succeed = True
        return True

    def save_location(self):
        return self.save_location_to(self.url)

    def save_location_to(self, url_out):
        exif_out = Exif(url_out)
        data_out = exif_out.exif
        if not exif_out.succeed:
            self.succeed = False
            self.error_info = exif_out.error_info
            return False

        if not self.has_gps_info():
            return False

        data_out["GPS"] = self.exif['GPS']

        return exif_out.save_to(url_out)

    def save_comment(self):
        return self.save_location_to(self.url)

    def save_comment_to(self, url_out):
        exif_out = Exif(url_out)
        if not exif_out.succeed:
            self.succeed = False
            self.error_info = exif_out.error_info
            return False

        comment = self.comment()
        if not self.succeed:
            self.succeed = False
            self.error_info = exif_out.error_info
            return False

        exif_out.set_comment(comment)
        return exif_out.save_to(url_out)

    def transplant_comment(self, exif_out) -> bool:
        comment = self.comment()
        if not self.succeed:
            return False

        return exif_out.set_comment(comment)

    def transplant_location(self, exif_out) -> bool:
        if not self.has_gps_info():
            return False
        if not exif_out.has_info():
            return False

        exif_out.exif['GPS'] = self.exif['GPS']
        self.succeed = True
        return True

    @staticmethod
    def transplant(input_url, output_url):
        try:
            piexif.transplant(input_url, output_url)
            return True
        except ValueError:
            return False

    @staticmethod
    def remove_all_and_save(url):
        piexif.remove(url)

    def remove_all(self):
        self.exif = {'0th': {}, 'Exif': {}, 'GPS': {}, 'Interop': {}, '1st': {}, 'thumbnail': None}
        self.succeed = True
        return True

    def remove_location(self):
        if not self.has_info():
            return False

        self.exif['GPS'] = {}
        self.succeed = True
        return True

    def remove_comment(self):
        if not self.has_exif_info():
            return False

        user_comment = piexif.helper.UserComment.dump('')
        self.exif['Exif'][piexif.ExifIFD.UserComment] = user_comment
        self.succeed = True
        return True

    def set_pic_time_by_str(self, start_time, stay_time, end_time):
        return self.set_comment(converter.rebuild_pic_time_by_str(start_time, stay_time, end_time))

    def set_pic_time(self, start_time, stay_time, end_time):
        return self.set_comment(converter.rebuild_pic_time(start_time, stay_time, end_time))

    def set_comment(self, comment):
        if not self.has_info():
            return False

        user_comment = piexif.helper.UserComment.dump(comment)
        self.exif['Exif'][piexif.ExifIFD.UserComment] = user_comment
        self.succeed = True
        return True

    def set_location(self, location):
        longitude, latitude = converter.str2location(location)
        return self.set_longitude_latitude(longitude, latitude)

    def set_longitude_latitude(self, longitude, latitude):
        if not self.has_info():
            return False

        self.exif["GPS"][piexif.GPSIFD.GPSLongitude] = converter.rebuild_location(longitude)
        self.exif["GPS"][piexif.GPSIFD.GPSLatitude] = converter.rebuild_location(latitude)

        self.succeed = True
        return True

    def has_info(self) -> bool:
        if self.exif is None or self.exif == {}:
            self.succeed = False
            self.error_info = 'no exif'
            return False
        else:
            self.succeed = True
            return True

    def has_gps_info(self) -> bool:
        if self.exif is None or self.exif == {} or self.exif['GPS'] == {}:
            self.succeed = False
            self.error_info = 'input is no location information in exif'
            return False
        else:
            self.succeed = True
            return True

    def has_exif_info(self) -> bool:
        if self.exif is None or self.exif == {} or self.exif['Exif'] == {}:
            self.error_info = 'no exif information'
            self.succeed = False
            return False
        else:
            self.succeed = True
            return True

    def is_jpeg(self, url) -> bool:
        try:
            i = Image.open(url)
            self.succeed = i.format == 'JPEG'
            return self.succeed
        except IOError:
            self.error_info = url + ' open failed'
            self.succeed = False
            return False
