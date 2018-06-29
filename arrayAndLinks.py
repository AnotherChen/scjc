# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 21:38:31 2018
数组与链表
@author: pc
"""
#一维数组
class Array:

    def __init__(self,size=30):
        self._size = size
        self._items = [None] * size

    def __getitem__(self,index):
        return self._items[index]

    def __setitem__(self,index,value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self,value= None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item

def test_array():
    size = 10
    a = Array(size)
    a[0] =1
    assert a[0] ==1
    print(a[0])
    a.clear()
    assert a[0] is None

#test_array()
#二维数组
class Array(object):
    def __init__(self,capacity,fillValue=None):
        self._items=list()
        for count in range(capacity):
            self._items.append(fillValue)
class Grid(object):
    def __init__(self,rows,columns,fillValue=None):
        self._data=Array(rows)
        for row in range(rows):
            self._data[row]=Array(columns,fillValue)
            
#table =Grid(4,5,0)
#print(table)

#单链表
class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q


    def getitem(self,index):

        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print('target is not exist!')

    def insert(self,index,item):

        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

    def index(self,value):

        if self.is_empty():
            print('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1


#l = LinkList()
#l.initlist([1,2,3,4,5])
#print(l.getitem(4))
#l.append(6)
#print(l.getitem(5))
#
#l.insert(4,40)
#print(l.getitem(3))
#print(l.getitem(4))
#print(l.getitem(5))
#
#l.delete(5)
#print(l.getitem(5))
#
#l.index(5)

#双链表
class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p
        self.prev = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def __getitem__(self, key):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print('the given key is error')
            return

        else:
            return self.getitem(key)



    def __setitem__(self, key, value):

        if self.is_empty():
            print('linklist is empty.')
            return

        elif key <0  or key > self.getlength():
            print('the given key is error')
            return

        else:
            self.delete(key)
            return self.insert(key)

    def initlist(self,data):

        self.head = Node(data[0])

        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            node.prev  = p
            p = p.next

    def getlength(self):

        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next

        return length

    def is_empty(self):

        if self.getlength() ==0:
            return True
        else:
            return False

    def clear(self):

        self.head = 0


    def append(self,item):

        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q
            q.prev = p


    def getitem(self,index):

        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next!=0 and j <index:
            p = p.next
            j+=1

        if j ==index:
            return p.data

        else:

            print('target is not exist!')

    def insert(self,index,item):

        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.prev = post
            q.next = p
            p.prev = q


    def delete(self,index):

        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index ==0:
            q = Node(item,self.head)

            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next
            p.next.prev = post

    def index(self,value):

        if self.is_empty():
            print('Linklist is empty.')
            return

        p = self.head
        i = 0
        while p.next!=0 and not p.data ==value:
            p = p.next
            i+=1

        if p.data == value:
            return i
        else:
            return -1

#
#l = LinkList()
#l.initlist([1,2,3,4,5])
#print(l.getitem(4))
#l.append(6)
#print(l.getitem(5))
#
#l.insert(4,40)
#print(l.getitem(3))
#print(l.getitem(4))
#print(l.getitem(5))
#
#l.delete(5)
#print(l.getitem(5))
#
#l.index(5)