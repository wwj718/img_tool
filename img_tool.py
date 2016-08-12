#!/usr/bin/env python
# encoding: utf-8
import os
import glob
import subprocess
import sys


'''
图片拼接工具，为美工组使用，用来制作类似游戏精灵的东西
跨平台 https://github.com/justbilt/convert2fnt

#todo
提花挪威Pillow
'''


convert = "convert"
options = "+append"
target = "dest.png"
IMG_TYPE = "png"

def img_splice(img_dir):
    command = []
    command.append(convert)
    command.append(options)

    img_list = glob.glob(img_dir+"/*.{}".format(IMG_TYPE))
    #filepath  = os.path.join(img_dir,filename)
    command.extend(img_list)

    command.append(target)

    print(command)
    subprocess.call(command)
    #convert +append u0.png u1.png u.png 拼接图片序列


if __name__ == '__main__':
    img_dir = sys.argv[1]
    img_splice(img_dir)
