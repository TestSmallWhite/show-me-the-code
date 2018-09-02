#!/sur/bin/env python3
# -*- conding: utf-8 -*-

"""
将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果

思路：
    1.首先使用一个可以载入图片的类获取图片的基础数据：（python2.7用PIL， python3用pillow）
        长
        宽
    2.根据长宽，计算合适的位置和字体大小
    3.生成数字幕布，把数字幕布和图片叠加在一起
        事实证明，字体不能离开幕布单独存在并和其他图像覆盖一起

        所以改变了一下策略：
            根据图像的大小生成一块圆形的幕布
            把字体和幕布覆盖
            幕布和图像覆盖
    4.生成新图片
"""

"""
总结一下：
    幕布和椭圆的大小比
        幕布有多大，椭圆有多大
        例如幕布是400，400这么大，那么椭圆的xy坐标就是[(0,0), (400,400)]

    数字和椭圆的位置比
        x = 120 /400 = 0.3
        y = 37 / 400 = 0.0925
        
    数字和椭圆的大小比
        300 / 400 = 0.75
"""

from PIL import Image, ImageDraw, ImageFont

import random, math

# #导入图像，确定图像的大小
# im = Image.open('day-oneTest.jpg')
#
# picWidth, picHeight = im.size
#
# #根据图像的大小，确定椭圆的位置
# new_width = picWidth * 0.85
# new_height = picHeight * 0.11
#
# #确定数字，随机0~9
# number = str(random.randint(0,9))
#
# #根据图像的大小，确定椭圆的大小
# #图像的w，h相乘，再乘以0.02，再开根号，那么就得到幕布的矩形大小
# #x=88, 88 7740  409600  = 0.02
# size = int(math.sqrt(int((picHeight * picWidth) * 0.02)))
#
# #确定字体大小
# font = ImageFont.truetype('arial.ttf', int(size * 0.75), encoding='utf-8')
#
# new_im = Image.new('RGB', (size, size), (255, 255, 255))
#
# draw = ImageDraw.Draw(new_im)
#
# draw.ellipse([(0,0), (size, size)], (255, 0, 0))
#
# draw.text((int(size * 0.3), int(size * 0.0925)), number, (255, 255, 255), font)
#
# new_im.save('modify.jpg', 'png')




#导入图像，确定图像的大小
im = Image.open('day-oneTest.jpg')

picWidth, picHeight = im.size

#根据图像的大小，确定椭圆的位置
new_width = picWidth * 0.85
new_height = picHeight * 0.11

#确定数字，随机0~9
number = str(random.randint(0,9))

#根据图像的大小，确定椭圆的大小
#图像的w，h相乘，再乘以0.02，再开根号，那么就得到幕布的矩形大小
#x=88, 88 7740  409600  = 0.02
size = int(math.sqrt(int((picHeight * picWidth) * 0.02)))
print(size)

#确定字体大小
font = ImageFont.truetype('arial.ttf', int(size * 0.75), encoding='utf-8')


draw = ImageDraw.Draw(im)

#draw.ellipse([(int(picWidth - size),0), (size, size)], (255, 0, 0))
draw.ellipse([(550,0), (640, 90)], (255, 0, 0), 0)

draw.text((560, 20), number, (255, 255, 255), font)

im.save('modify.jpg', 'png')