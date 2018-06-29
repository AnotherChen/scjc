# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:19:30 2018
栈
@author: pc
"""
class Stack(object):
    # 初始化栈为空列表
    def __init__(self):
        self.items = []

    # 判断栈是否为空，返回布尔值
    def is_empty(self):
        return self.items == []

    # 返回栈顶元素
    def peek(self):
        return self.items[len(self.items) - 1]

    # 返回栈的大小
    def size(self):
        try:
            return len(self.items)
        except:
            return 0
    # 把新的元素堆进栈里面（程序员喜欢把这个过程叫做压栈，入栈，进栈……）
    def push(self, item):
        self.items.append(item)

    # 把栈顶元素丢出去（程序员喜欢把这个过程叫做出栈……）
    def pop(self, item):
        return self.items.pop()


if __name__ == "__main__":
    # 初始化一个栈对象
    my_stack = Stack()
    # 把'h'丢进栈里
    my_stack.push('h')
    # 把'a'丢进栈里
    my_stack.push('a')
    # 看一下栈的大小（有几个元素）
    print(my_stack.size())
    # 打印栈顶元素
    print(my_stack.peek())
    # 把栈顶元素丢出去，并打印出来
    print(my_stack.pop('a'))
    # 再看一下栈顶元素是谁
    print(my_stack.peek())
    # 这个时候栈的大小是多少？
    print(my_stack.size())
    # 再丢一个栈顶元素
    print(my_stack.pop('h'))
    # 看一下栈的大小
    print(my_stack.size)
    # 栈是不是空了？
    print(my_stack.is_empty())
    # 哇~真好吃~
    print('Yummy~')
