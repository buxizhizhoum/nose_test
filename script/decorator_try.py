#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
把装饰器看成是一个接收函数名作为输入参数并且返回一个函数
"""
import time
import datetime


def logged(time_format):
    # add one more parameter needs one more closure? yes.
    def decorator(func):
        def decorated_func(*args, **kwargs):
            print "- Running '%s' on %s " % (
                func.__name__,
                time.strftime(time_format)
            )

            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()

            print "- Finished '%s', execution time = %0.3fs " % (
                func.__name__,
                end_time - start_time
            )

            return result

        decorated_func.__name__ = func.__name__
        return decorated_func

    return decorator


def ticker(func):
    # accept a function as parameter
    def print_info(*args, **kwargs):
        # do something before
        print "- Started '%s' on %s " % (
            func.__name__,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        )

        start_time = time.time()

        # run function
        result = func(*args, **kwargs)

        # do something after
        end_time = time.time()

        print "- Finished '%s' on %s" % (
            func.__name__,
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        )
        print "Time consumed: %0.3f second(s)" % (end_time - start_time)
        return result

    print_info.__name__ = func.__name__
    # return the result of decorated_func which is result of func.
    return print_info


@logged("%b %d %Y - %H:%M:%S")
def add1(x, y):
    time.sleep(1)
    return x + y

print add1(1, 2)


@ticker
def add2(x, y):
    time.sleep(1)
    return x + y

print add2(1, 2)
