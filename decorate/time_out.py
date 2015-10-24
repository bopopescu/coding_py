#!/usr/bin/env python
#coding=utf-8

import signal,functools,time
class TimeoutError(Exception):pass

def timeout(seconds, error_message = 'Function call timed out'):
    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)
    return decorated

@timeout(5)
def sleep():
    time.sleep(0.5)
    time.sleep(6)
sleep()
