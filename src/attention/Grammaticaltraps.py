#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by kuroky on 2021/3/22


def arrays():
    '''
    +是指把两个序列的元素拼接在一起。通常+号两侧的序列由相同类型的数据所构成，在拼接的过程中，
    两个被操作的序列都不会被修改，Python会新建一个包含同样类型数据的序列作为拼接的结果
    :return:
    '''
    a = [1]
    b = [2]
    c = a + b
    print(a, b, c)
    print(id(a), id(b), id(c))

    '''
    如果想要把一个序列复制几份然后再拼接起来，更快捷的做法是把这个序列乘以一个整数。同样，这个操作会产生一个新序列
    '''


def lists():
    '''
给my_list的最后一个元素的列表赋值，结果所有三个元素的列表都被赋值了！这反映出my_list这三个元素不是3个列表，而是3个列表引用，指向了同一个相同的列表
    :return:
    '''
    x = ["x"]
    my_list = [x] * 3
    print(my_list)  # [['x'], ['x'], ['x']]

    x2 = my_list[2]
    x2[0] = "y"
    print(my_list)


if __name__ == '__main__':
    arrays()
    lists()
    pass
