#!/usr/bin/env python3
#coding=utf-8

def jumping_range(up_to):
    index = 0
    while index < up_to:
        jump = yield index
        print("jump")
        print(jump)
        print("------")
        if jump is None:
            jump = 1
        index += jump

def my_range(up_to):
    index = 0
    def loop():
        while index < up_to:
            yield index
            index += 1
    yield from loop()

def wait_index(i):
    print("waiting")
    return (yield i)

def jumping_range_2(up_to):
    index = 0
    while index < up_to:
        jump = yield from wait_index(index)
        print("jump")
        print(jump)
        print("-----")
        if jump is None:
            jump = 1
        index += jump

if __name__ == '__main__':
    #iterator = jumping_range(5)
    #print(next(iterator)) #0
    #print(iterator.send(2)) #2

    iterator_2 = jumping_range_2(5)
    print(iterator_2)
    print(iterator_2.send(None))
