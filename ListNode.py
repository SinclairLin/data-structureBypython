# -*- coding: utf-8 -*-

"""
@author: SinclairLin
@software: PyCharm
@file: ListNode.py
@time: 2022/8/26 10:09
"""


class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    # 反转单向链表
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
