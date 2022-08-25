# -*- coding: utf-8 -*-

"""
@author: SinclairLin
@software: PyCharm
@file: Stack.py
@time: 2022/8/25 10:09
"""


# 栈类
class Stack:
    # 初始化
    def __init__(self):
        self.item = []

    # 若空，返回TRUE
    def is_empty(self):
        return self.item == []

    def push(self, item):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    # 返回栈顶元素
    def peek(self):
        return self.item[len(self.item) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.item)


s = Stack()
print(s.is_empty())  # True
s.push(9)
print(s.is_empty())  # False
s.push('1! 5!')
print(s.size())  # 2
print(s.peek())  # 1! 5!
print(s.pop())  # 1! 5!


def turn_string(my_str):
    s2 = Stack()
    output_str = ''
    for i in my_str:
        s2.push(i)
    while not s2.is_empty():
        output_str += s2.pop()
        return output_str

