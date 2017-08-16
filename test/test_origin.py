#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from bin.data_process import DataProcessor


data_processor = DataProcessor()


def setUp():
    print "function setup"
    # raise ZeroDivisionError


def tearDown():
    print "function teardown"
    # raise ZeroDivisionError


def test_add():
    assert (1 + 2) == data_processor.add(1, 2)


def test_decrease():
    assert (1 - 2) == data_processor.decrease(1, 2)


def test_multiply():
    assert (1 * 2) == data_processor.multiply(1, 2)
    # sys.exit(0)


def test_div():
    assert (2/1) == data_processor.div(2, 1)
    assert data_processor.div(1, 0) is ZeroDivisionError


def test_div_zero():
    assert data_processor.div(1, 0) is ZeroDivisionError


def test_div_zero_1():
    try:
        data_processor.div(1, 0)
    except Exception as e:
        assert e is ZeroDivisionError


class Test(object):
    def setUp(self):
        print "MyTestClass setup"

    def tearDown(self):
        print "MyTestClass teardown"

    def test_div(self):
        try:
            data_processor.div(1, 0)
        except Exception as e:
            assert e is ZeroDivisionError

    def test_div_zero(self):
        assert data_processor.div(1, 0) is ZeroDivisionError
