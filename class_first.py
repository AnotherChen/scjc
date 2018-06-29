# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:39:25 2018
类的定义及使用（一）
@author: pc
"""

class Counter(object):
    instances=0
    def __init__(self):
        Counter.instances+=1
        self.reset()
    
    def reset(self):
        self._value=0

    def increment(self,amount=1):
        self._value+=amount
        
    def decrement(self,amount=1):
        self._value-=amount
        
    def getValue(self):
        return self._value
    
    def __str__(self):
        return str(self._value)
    
    def __eq__(self,other):
        if self is other:return True
        if type(self) !=type(other):return False
        return self._value==other._value

    










