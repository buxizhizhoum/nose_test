#!/usr/bin/python
# -*- coding: utf-8 -*-

import math


class Calculator(object):
    def __init__(self):
        pass

    def add(self, *args):
        # print args
        return sum(args)

    def sub(self, x, y):
        return x - y

    def time(self, x, y):
        return x * y

    def div(self, x, y):
        try:
            return x/y
        except ZeroDivisionError as e:
            return e

if __name__ == "__main__":
    cal = Calculator()
    print cal.add(1, 2)
