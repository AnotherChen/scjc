# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:01:25 2018
队列
@author: pc
"""

'''队列的列表实现'''
class Queue:
    """A list_based queue implementation."""
    
    # Constructor
    def __init__(self):
        """Sets the initial state of self,and the initial state is []"""
        self.items = []
    
    # Accessor methods
    def iter(self):
         """Supports iteration over a view of self.
         Visits items from bottom to top of queue."""
         for i in range(len(self.items)):
             yield self.items[i]
         
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self.items)==0
 
    def peek(self):
        """
        Returns the item at the top of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self.items[0]
     
    def size(self):
        """return the len(self)"""
        return len(self.items)
    
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.items = []
        
    def add(self, item):
        """Adds item to the top of the queue."""
        self.items.append(item)
   
    def pop(self):
        """
        Removes and returns the item at the top of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the top item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self.items.pop(0) 
    
if __name__=='__main__':
    q=Queue()
    q.add(1)
    q.add(2)
    q.add(3)
    print(list(q.iter()))       #return:[1,2,3]
    print(q.size())             #return:3
    print(q.pop())              #return:1
    print(q.peek())             #return:2
    print(q.pop())              #return:2
    print(q.pop())              #return:3
    #若在此处添加一句：q.pop()或q.peek()，将报错："The queue is empty."
    q.clear()
    print(q.isEmpty())     

'''队列的链表实现'''
class Node(object):
    """Nodes for singly linked structures."""
 
    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None"""
        self.data = data
        self.next = next
 
class AbstractCollection(object):
    """An abstract collection implementation."""
 
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
 
    # Accessor methods
    def __len__(self):
        """-> The number of items in self."""
        return self._size
 
    def isEmpty(self):
        return len(self) == 0
 
    def __str__(self):
        """Returns the string representation of self."""
        return "[" + ", ".join(map(str, self)) + "]"
 
    def __add__(self, other):
        """Returns a new collection consisting of the
        items in self and other."""
        result = type(self)(self)
        for item in other:
            result.add(item)
        return result
 
    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        otherIter = iter(other)
        for item in self:
            if item != next(otherIter):
                return False
        return True
 
class LinkedQueue(AbstractCollection):
    """A link-based queue implementation."""
 
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._front = self._rear = None
        AbstractCollection.__init__(self, sourceCollection)
 
    # Accessor methods
    def __iter__(self):
        """Supports iteration over a view of self."""
        pass
    
    def peek(self):
        """
        Returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the stack is empty."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        return self._front.data
 
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        pass
    
    def add(self, item):
        """Adds item to the rear of the queue."""
        newNode = Node(item, None)
        if self.isEmpty():
            self._front = newNode
        else:
            self._rear.next = newNode
        self._rear = newNode
        self._size += 1
 
    def pop(self):
        """
        Removes and returns the item at the front of the queue.
        Precondition: the queue is not empty.
        Raises: KeyError if the queue is empty.
        Postcondition: the front item is removed from the queue."""
        if self.isEmpty():
            raise KeyError("The queue is empty.")
        oldItem = self._front.data
        self._front = self._front.next
        if self._front is None:
            self._rear = None
        self._size -= 1
        return oldItem    

'''Python内部的四个队列'''
#from queue import Queue #LILO队列
#q = Queue() #创建队列对象
#q.put(0)    #在队列尾部插入元素
#q.put(1)
#q.put(2)
#print('LILO队列',q.queue)  #查看队列中的所有元素
#print(q.get())  #返回并删除队列头部元素
#print(q.queue)

#from queue import LifoQueue #LIFO队列
#lifoQueue = LifoQueue()
#lifoQueue.put(1)
#lifoQueue.put(2)
#lifoQueue.put(3)
#print('LIFO队列',lifoQueue.queue)
#lifoQueue.get() #返回并删除队列尾部元素
#lifoQueue.get()
#print(lifoQueue.queue)
#
#from queue import PriorityQueue #优先队列
#priorityQueue = PriorityQueue() #创建优先队列对象
#priorityQueue.put(3)    #插入元素
#priorityQueue.put(78)   #插入元素
#priorityQueue.put(100)  #插入元素
#print(priorityQueue.queue)  #查看优先级队列中的所有元素
#priorityQueue.put(1)    #插入元素
#priorityQueue.put(2)    #插入元素
#print('优先级队列:',priorityQueue.queue)  #查看优先级队列中的所有元素
#priorityQueue.get() #返回并删除优先级最低的元素
#print('删除后剩余元素',priorityQueue.queue)
#priorityQueue.get() #返回并删除优先级最低的元素
#print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
#priorityQueue.get() #返回并删除优先级最低的元素
#print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
#priorityQueue.get() #返回并删除优先级最低的元素
#print('删除后剩余元素',priorityQueue.queue)  #删除后剩余元素
#priorityQueue.get() #返回并删除优先级最低的元素
#print('全部被删除后:',priorityQueue.queue)  #查看优先级队列中的所有元素
#
#from collections import deque   #双端队列
#dequeQueue = deque(['Eric','John','Smith'])
#print(dequeQueue)
#dequeQueue.append('Tom')    #在右侧插入新元素
#dequeQueue.appendleft('Terry')  #在左侧插入新元素
#print(dequeQueue)
#dequeQueue.rotate(2)    #循环右移2次
#print('循环右移2次后的队列',dequeQueue)
#dequeQueue.popleft()    #返回并删除队列最左端元素
#print('删除最左端元素后的队列：',dequeQueue)
#dequeQueue.pop()    #返回并删除队列最右端元素
#print('删除最右端元素后的队列：',dequeQueue)