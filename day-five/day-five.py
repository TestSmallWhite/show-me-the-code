"""

题目：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小

实现：
    os内置模块有很多实用的方法

    os.getcwd()：查看当前所在路径。

    os.listdir(path):列举目录下的所有文件。返回的是列表类型

    os.path.abspath(path):返回path的绝对路径

    os.path.split(path):将路径分解为(文件夹,文件名)，返回的是元组类型。可以看出，若路径字符串最后一个字符是\,则只有文件夹部分有值；
    若路径字符串中均无\,则只有文件名部分有值。若路径字符串有\，且不在最后，则文件夹和文件名均有值。且返回的文件夹的结果不包含\.

    os.path.join(path1,path2,...):将path进行组合，若其中有绝对路径，则之前的path将被删除

    os.path.dirname(path):返回path中的文件夹部分，结果不包含'\'

    os.path.basename(path):返回path中的文件名。

    os.path.getmtime(path):文件或文件夹的最后修改时间，从新纪元到访问时的秒数。

    os.path.getatime(path):文件或文件夹的最后访问时间，从新纪元到访问时的秒数。

    os.path.getctime(path):文件或文件夹的创建时间，从新纪元到访问时的秒数

    os.path.getsize(path):文件或文件夹的大小，若是文件夹返回0

    os.path.exists(path):文件或文件夹是否存在，返回True 或 False

    os中定义了一组文件、路径在不同操作系统中的表现形式参数



    我们只需要根据传入的路径，找到以“jpg、jpeg、png”后缀的文件
        os.listdir(path) 返回的是目录下所有文件，所以还需要判断一下文件的后缀

    获取文件的长宽
        Image.open(path)

    判断文件的长宽是否大于1136*640
        如果大于就
            文件的最大值对应1136
            文件的最小值对应640
        小于就不管了

    不管修不修改都保存到另外一个新文件夹中
        os.makedirs()
"""
import os
from PIL import Image

def modifyPic(modifyAgoPath, modifyAfterPath, width = 1136, height = 640):
    """
    :param modifyAgoPath: 存放待修改的图片路径
    :param modifyAfterPath: 修改后存放图片的路径
    :param width:   指定图片的长
    :param height:  指定图片的高
    :return:
    """
    #根据modifyAgoPath，去该路径下找到所有的以“jpg、jpeg、png”后缀的文件，并保存到一个list中
    modifyFile = [x for x in os.listdir(modifyAgoPath) if x.find('.JPG') >= 0 or x.find('.PNG') >= 0 or x.find('.JPEG') >= 0]

    #拿到图片后，循环修改图片
    for x in modifyFile:
        im = Image.open(modifyAgoPath + '\\' + x)

        width, height = im.size

        if width >= height:
            if width > 1136:
                width = 1136
        else:
            if height > 640:
                height = 640

        #im.thumbnail((str(width), str(height)))
        im.thumbnail((width, height))

        im.save(modifyAfterPath + '\\' + x )

if __name__ == '__main__':
    modifyPic(r'E:\Git-codeBase\show-me-the-code\day-five\test', r'E:\Git-codeBase\show-me-the-code\day-five\test2')