# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 17:03:29 2018
搜索算法
@author: pc
"""
#搜索最小值
def indexOfMin(lyst):
    minIndex=0
    currentIndex=1
    while currentIndex<len(lyst):
        if lyst[minIndex]>lyst[currentIndex]:
            minIndex=currentIndex
        currentIndex+=1
    #print(lyst[minIndex])
    return minIndex

#minIn=indexOfMin([1,2,3,0,5])
#print(minIn)

#搜索算法之一：顺序搜索
def sequenceSearch(target,lyst):
    position=0
    while position<len(lyst):
        if lyst[position]==target:
            return position
        position+=1
    return -1

#pos=sequenceSearch(3,[1,4,2,3,2])
#print(pos)

#搜索算法之二：二叉搜索（有序列表）
def biSearch(target,lyst):
    left=0
    right=len(lyst)-1
    while left<=right:
        mid=(left+right)//2
        if target==lyst[mid]:
            return mid
        elif target<lyst[mid]:
            right=mid-1
        else:
            left=mid+1
    return -1

#mid=biSearch(8,[1,3,4,8,10])
#print(mid)

#比较数据项
class SaveAccount(object):
    def __init__(self,name,pin,balance=0.0):
        self._name=name
        self._pin=pin
        self._balance=balance
        
    def __lt__(self,other):
        return self._name<other._name
    
#fibonacci之一：简单递归
def fib1(n):
    if n in [0,1]:
        return n
    return fib1(n-1) + fib1(n-2)

#print(fib(10))

#fibonacci之二：优化递归
f_num = {}
def fib2(n):
    #print(f_num)
    #print(n)

    if n in [0,1]:
        f_num[n] = n
        return f_num[n]
    elif n in f_num:
        print(f_num[n])
        return f_num[n]
    else:
        f_num[n] = fib2(n-1) + fib2(n-2)
        return f_num[n]

#print(fib(986))

#fibonacci之三：迭代
def fib_iter(n):
    pre = 1
    next = 1
    result = 0
    i = 2
    while i < n:
        result = pre + next
        pre = next
        next = result
        i += 1
    return result

#print(fib_iter(986))