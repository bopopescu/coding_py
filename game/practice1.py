#!.usr/bin/python
#coding=utf-8


class unit:
    def __init__(self):
        self.blood_max = self.blood
        print self.name + " created"
class attacker(unit):
    def attack(self, u):
        u.blood -= self.dps
        if u.blood <= 0:
            print u.name + " was dead!!!"
            del u
        else:
            print u.name + " was attacked! __bool = " + str(u.blood)
class boomer(attacker):
    def __init__(self, name):
        self.name = name
        self.blood = 50
        self.dps = 20
        unit.__init__(self)
    def boom(self, u):
        u.blood -= self.dps
        if u.blood <= 0:
            print u.name + " was dead!!!"
            del u
        print self.name + " was boom!!"
        del self
class machineGun(attacker):
    def __init__(self, name):
        self.blood = 100
        self.name = name
        unit.__init__(self)
        self.dps = 30
        print self.name + " created"
class tree(unit):
    def __init__(self, name):
        self.name = name
        print self.name + " created"
class healer(unit):
    def __init__(self, name):
        self.name = name
        self.blood = 50
        unit.__init__(self)
        self.hps = 15
        print self.name + " created"
    def heal(self, u):
        u.blood += self.hps
        if u.blood >= u.blood_max:
            u.blood = u.blood_max
        print u.name + " was healed ! __blood = " + str(u.blood)
j1 = machineGun("j1")
b1 = boomer("b1")
b1.boom(j1)
