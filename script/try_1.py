#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import time


def print_time(func):
    # function
    def function_1(x, y):
        # parameters
        print datetime.datetime.now()

        res = func(x, y)

        print datetime.datetime.now()
        return res

    return function_1


@print_time
def add(x, y):
    time.sleep(1)
    res = x + y
    return res

add(1, 2)
