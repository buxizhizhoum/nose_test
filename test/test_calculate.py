#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from bin.calculate import Calculator


class Test(object):
    def setUp(self):
        self.calculator = Calculator()
        print "MyTestClass setup"

    def tearDown(self):
        print "MyTestClass teardown"

    def test_add(self):
        assert (1 + 2) == self.calculator.add(1, 2)

    def test_sub(self):
        assert (1 - 2) == self.calculator.sub(1, 2)

    def test_time(self):
        assert (1 * 2) == self.calculator.time(1, 2)

    def test_div(self):
        try:
            self.calculator.div(1, 0)
        except Exception as e:
            assert e is ZeroDivisionError

    # def test_div_zero(self):
    #     assert self.calculator.div(1, 0) is ZeroDivisionError

