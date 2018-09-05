"""
0004题：任一个英文的纯文本文件，统计其中的单词出现的个数。

分析：
    一般的英语文章，会包含：
        大小写字母
        数字
        符号：
            结束性符号（遇到这种符号可以结束判断单词的）
            , . !  -- ;(分号) :（冒号） ? ... ()  (空格) "" '' /

                因为统计需要再细分一下结束性符号， 分为遇到一次就可以统计，和需要遇到两次才能结束统计
                    统计一次：
                        , . ! -- ;(分号) :（冒号） ? ...  (空格) /
                    统计两次：
                        -- () "" ''

            需要多次判断的符号
            '(单引号，例如don't) -(连词符，一般用于换行时连接字母)

    遇到结束性的符号时可能就是一个单词了

实现：
    用字典记录每个符号，单词出现的次数

    需要注意单引号和连词符，这两个和单词是一个整体，不能分割

    还有像"" '' () -- 需要注意，特别是'' 在判断的时候可以会和' 搞混了
        怎么区分' ''呢？
        一个单引号时，后面肯定是只接一个字母或者数字
        成对单引号，后面再进行多次判断，可能有以下场景：
            '8'
            'asd'
"""

# import string
#
# #先定义字典
# count_one = {
#     ',' : 0,
#     '.' : 0,
#     '!' : 0,
#     '--': 0,
#     ';': 0,
#     ':': 0,
#     '?': 0,
#     '...': 0,
#     ' ': 0,
#     '/': 0
# }
#
# count_two = {
#     '\'\'' : 0,
#     '\"\"' : 0,
#     '--' : 0,
#     '()' : 0
# }
#
# other = {
#     '\'' : 0,
#     '-' : 0
# }
#
# #用来存储英文的次数
# word = {}
#
# #用来临时存储英文的字母
# linshi = ''
#
# #path是文件的路径
# def count(path):
#
#     global linshi
#
#     with open(path, 'r') as f:
#         for x in f:
#             for y in x:
#                 if y in (string.ascii_letters or string.digits):
#                     linshi = linshi + str(y)
#                 elif y in (count_one.keys() or other.keys() or count_two.keys()):
#                     if linshi == '':
#                         pass
#                     elif  word.get(linshi, None) == None:
#                         word[linshi] = 1
#                         linshi = ''
#                     elif word.get(linshi) > 0:
#                         word[linshi] = word[linshi] + 1
#                         linshi = ''
#
#
# if __name__ == '__main__':
#     count(r'C:\Users\V_ZIWCAO\Desktop\test.txt')
#
#     print(word)


#其他人的代码：
import re
from collections import Counter


def word_count(txt):
    word_pattern = r'[a-zA-Z-]+'
    words = re.findall(word_pattern, txt)
    print(words)
    return Counter(words).items()

if __name__ == '__main__':
    #这个不太好，把所有的字母都变成小写了
    #txt = open(r'C:\Users\V_ZIWCAO\Desktop\test.txt', 'r').read().lower()

    txt = open(r'C:\Users\V_ZIWCAO\Desktop\test.txt', 'r').read()
    print (word_count(txt))

