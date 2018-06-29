# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 15:53:06 2018
类的定义及使用（二）
@author: pc
"""

#from class_first import Counter

class Employee:
    empCount=0#创建的实例个数
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount+=1
    def displayCount(self):
        print("Total Employee %d" % self.empCount)
    def displayEmployee(self):
        print("Name : ", self.name,  ", Salary: ", self.salary)

emp1 = Employee("Zara", 2000)
"创建 Employee 类的第二个对象"
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()        