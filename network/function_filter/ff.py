#!/usr/bin/env python
#coding=utf-8

import sys, os, json
import conf


sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet import nbNet

alarmStatus = {}

def ff(d_in):
    
    mon_data = json.loads(d_in)
    #print mon_data
    for rule in conf.ff_conf:
        monKey, operator, value, alarmRecv = rule
        monName = monKey + operator + str(value)
        eval_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(eval_function)
        if ff_result:
            alarmStatus[monName] = True
            print "Alarm", eval_function, alarmRecv
        else:
            if (alarmStatus.get(monName, False)):
                alarmStatus[monName] = False
                print "Recover", eval_function, alarmRecv

if __name__ == '__main__':
    def logic(d_in):
        ff(d_in)
        print("ok")

    ffD = nbNet('0.0.0.0', 5000, logic)
    ffD.run()
