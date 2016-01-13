#!/usr/bin/env python3
#coding=utf-8

import redis

def connect_handle(_host, _port):
    return redis.Redis(host=_host, port=_port, db=0)

def search(redis_key, conn, filter_key = None, filter_value = None):
    redis_data = eval(conn[redis_key])

    if not filter_key or not filter_value:
        return redis_data
    else:
        result = []
        for redis_key, redis_value in redis_data.items():    
            if str(redis_value[filter_key]) == str(filter_value):
                result.append(redis_value)

        return result

if __name__ == '__main__':
    HOST = '127.0.0.1'
    PORT = 6379
    redis_key = "2015-11-24-T002-union-dispatch"
    filter_key = 'spu_id'
    filter_value = 'C03998'

    r = connect_handle(HOST, PORT)

    print(search(redis_key, r, filter_key, filter_value))
