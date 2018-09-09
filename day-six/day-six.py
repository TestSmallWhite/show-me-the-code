"""

第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来

分析：
    空行好说，遇到就+1
    
    注释：
        注释分单行注释和多行注释，单行注释用# 多行注释用'""""""'
        
        单行注释：
            分几种情况：
                开头第一个符号就是#，或者前面有一些空格然后才是#
                    统计到单行注释中
                
                这一行前面是代码，后面是注释
                    这个就算到是代码行里吧，多次统计会总额不对的，或者在字典中加一个键对值记录一下
                    
        多行注释：
            只有一行的多行注释：
                多行注释+1
            n行以上的多行注释：
                遇到\"""就询问一个变量，是不是开始，然后直到遇到另一半\"""后+1操作
"""

import os

def countSpaceOrNote(filePath, fileTyoe = 'py',saveCount = None):
    """
    :param filePath: 文件存放的路径
    :param fileTyoe: 需要统计的文件类型，默认是py文件
    :param saveCount: 将统计结果保存到某个路径上的文件，默认是None
    :return:
    """

    count = {
        'total' : 0,
        'space' : 0,
        'danNote' : 0,
        'duoNote' : 0,
        'toalDuoHangNoteTime' : 0
    }

    isDuoHangNote = False
    isTongYiHang = True

    #第一二三个双引号，当三个都是true时，表示遇到了多行注释符号
    one = [False, 0]
    two = [False, 0]
    three = [False, 0]

    file = [x for x in os.listdir(filePath) if x.find('.'+ fileTyoe) >= 0]

    for y in file:
        with open(os.path.join(filePath, y), 'r', encoding='utf-8') as f:
            for z in f:  # 遍历行
                count['total'] = count['total'] + 1

                if isDuoHangNote:
                    count['duoNote'] = count['duoNote'] + 1
                else:
                    isTongYiHang = True

                if z == '\n':
                    count['space'] = count['space'] + 1
                    continue

                num = 0

                for q in z:  # 遍历每个字符
                    num = num + 1
                    if q == '#':
                        count['danNote'] = count['danNote'] + 1
                        continue
                    elif q == '"':
                        if not one[0]:
                            one[0] = True
                            one[1] = num
                        elif not two[0]:
                            if one[1] + 1 == num:
                                two[0] = True
                                two[1] = num
                            else:
                                one[0] = False
                                one[1] = 0
                        else:
                            if two[1] + 1 == num:
                                if isDuoHangNote and isTongYiHang:
                                    # 如果同一行遇到isDuoHangNote 和 isTongYiHang = True表示，多行注释在一行就已经结束了
                                    isDuoHangNote = False
                                    count['toalDuoHangNoteTime'] = count['toalDuoHangNoteTime'] + 1
                                elif not isDuoHangNote:
                                    isDuoHangNote = True
                                else:
                                    isDuoHangNote = False
                                    count['toalDuoHangNoteTime'] = count['toalDuoHangNoteTime'] + 1

                            one[0] = False
                            one[1] = 0
                            two[0] = False
                            two[1] = 0

                            count['duoNote'] = count['duoNote'] + 1

                            isTongYiHang = False


    count['duoNote'] = count['duoNote'] - count['toalDuoHangNoteTime']
    print(count)

if __name__ == '__main__':
    countSpaceOrNote(r'E:\Git-codeBase\show-me-the-code\day-five')


