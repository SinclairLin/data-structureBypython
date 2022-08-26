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
        self.top = -1
        self.item = []

    # 若空，返回TRUE
    def is_empty(self):
        return self.item == []

    def push(self, item: any):
        self.item.append(item)

    def pop(self):
        return self.item.pop()

    # 返回栈顶元素
    def peek(self):
        return self.item[len(self.item) - 1]

    # 返回栈的大小
    def size(self):
        return len(self.item)

    # 将栈置空
    def empty(self):
        self.item = []
        self.top = -1


# s = Stack()
# print(s.is_empty())  # True
# s.push(9)
# print(s.is_empty())  # False
# s.push('1! 5!')
# s.empty()
# print(s.size())
# print(s.size())  # 2
# print(s.peek())  # 1! 5!
# print(s.pop())  # 1! 5!


# 通过栈反转字符串
def turn_string(my_str: str):
    s = Stack()
    output_str = ''
    for i in my_str:
        s.push(i)
    while not s.is_empty():
        output_str += s.pop()
    return output_str


# print(turn_string('理塘丁真'))
# print(turn_string('逆天邪神'))
# print(turn_string('KFC CRAZY TUS, V ME 50'))


# 通过栈判断左右括号是否匹配
def par_checker(par: str):
    s = Stack()
    flag = True
    index = 0
    while flag and index < len(par):
        symbol = par[index]
        if symbol in '([{':
            s.push(symbol)
        elif s.is_empty():
            flag = False
        else:
            top = s.pop()
            if not matches(top, symbol):
                flag = False
        index += 1
    return bool(flag and s.is_empty())


def matches(left, right):
    lp = '([{'
    rp = ')]}'
    return lp.index(left) == rp.index(right)


# print(par_checker('([{)]}'))  # False
# print(par_checker('{[()]}'))  # True
# print(par_checker('({([()])}){}'))  # True


# 通过栈实现进制转换
def base_conversion(d_number: int, base: int):
    digits = '0123456789ABCDEF'
    s = Stack()
    while d_number > 0:
        s.push(d_number % base)  # 取余，然后入栈
        d_number //= base  # 整除
    string = ''
    while not s.is_empty():
        string += digits[s.pop()]
    return string

# print(base_conversion(666, 16))  # 29A
# print(base_conversion(666, 5))  # 10131
# print(base_conversion(666, 8))  # 1232
