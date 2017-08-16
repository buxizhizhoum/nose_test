#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
import nose


class DataProcessor(object):
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def decrease(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a * b

    def div(self, a, b):
        if b != 0:
            return a/b
        else:
            return ZeroDivisionError

if __name__ == "__main__":
    assert 1 == 1
    print "aaa"


