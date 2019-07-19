# _*_ coding=utf-8 _*_


def binary_search(data, val):
    """
    二分查找：二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。
            但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。
    时间复杂度：O(log n)
    :param data: 有序列表
    :param val: 目标值
    :return: 索引
    """
    left = 0                          # 最小下标数
    right = len(data) - 1             # 最大下标数

    while left <= right:
        mid = left + right // 2       # 中间下标数，将列表分成两个区域

        if data[mid] == val:          # 中间下标数等于val，返回
            return mid
        elif data[mid] > val:         # 元素在左边区域，移动right下标，锁定查找范围在左边区域
            right = mid - 1
        else:
            left = mid + 1            # 元素在右边区域，移动left下标，锁定查找范围在右边区域

    else:                             # 循环结束，列表内元素全部搜索完，没有找到val
        return
