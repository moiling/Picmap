#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-07 14:38
# @Author  : moiling
# @File    : testExifComment.py
from libPicmap.exif import Exif

with_comment = '/Users/moi/Downloads/1.jpg'
without_Comment = '/Users/moi/Downloads/2.jpg'

if __name__ == '__main__':
    print('-----测试获取有comment图片-----')
    print(Exif(with_comment).comment())

    print('-----测试获取无Comment图片-----')
    noComment = Exif(without_Comment)
    print(noComment.comment())
    print(noComment.error_info)

    print('-----测试添加时间信息,单位分钟(仅内存)-----')
    comment = Exif(with_comment)
    comment.set_pic_time(80, 100, 200)
    print(comment.pic_time())
    # 重读一次
    comment = Exif(with_comment)
    print(comment.pic_time())

    print('-----测试添加时间信息,时间格式(仅内存)-----')
    comment.set_pic_time_by_str('8:56', '1:03', '16:33')
    print(comment.pic_time())
    # 重读一次
    comment = Exif(with_comment)
    print(comment.pic_time())

    print('-----测试转移Comment(仅内存)--------')
    comment.transplant_comment(noComment)
    print(noComment.pic_time())
    # 重新读一次
    noComment = Exif(without_Comment)
    print(noComment.pic_time())

    print('-----测试转移Comment(只外存保存)--------')
    comment.save_comment_to(without_Comment)
    print(noComment.pic_time())
    # 重新读一次
    noComment = Exif(without_Comment)
    print(noComment.pic_time())

    print('-----测试设置Comment(仅内存)--------')
    noComment.set_comment('hello')
    print(noComment.comment())
    print('-----保存在外存--------')
    noComment.save()
    # 重新读一次
    noComment = Exif(without_Comment)
    print(noComment.comment())

    print('-----测试只将Comment改动保存在外存--------')
    # 对location也做一些改动
    noComment.set_location('23.048562,113.405411')
    noComment.set_comment('yes')
    print(noComment.location())
    print(noComment.comment())
    noComment.save_comment()
    # 重新读一次
    noComment = Exif(without_Comment)
    print(noComment.location())
    print(noComment.comment())

    print('-----测试删除Comment(只内存保存)--------')
    noComment.remove_comment()
    print(noComment.comment())
    print('-----保存在外存--------')
    noComment.save()
    # 重新读一次
    noComment = Exif(without_Comment)
    print(noComment.comment())



