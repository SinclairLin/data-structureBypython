# -*- coding: utf-8 -*-

"""
@author: SinclairLin
@software: PyCharm
@file: String.py
@time: 2022/8/26 9:34
"""


class String:

    def __init__(self):
        self.list = []
        self.item = ''

    def load(self, input_str: str):
        self.item = input_str

    def size(self):
        return len(self.item)

    def search(self, left: int, right: int):
        return self.item[left: right]


s = String()
(s.load('niewenhao'))
print(s.size())
print(s.search(3, 9))
