# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 19:48:22 2018
排序算法
@author: pc
"""

#1 选择排序（老师给小学生排一队）
from search import indexOfMin
def swap(lyst,i,j):
    temp=lyst[i]
    lyst[i]=lyst[j]
    lyst[j]=temp
    
def selectSort(lyst):
    i=0
    while i<len(lyst)-1:
        minIndex=indexOfMin(lyst[i:])
        realIndex=i+minIndex
        #print(minIndex)
        swap(lyst,i,realIndex)
        i+=1

sel=[2,3,0,1,9,11,4]
#selectSort(sel)
#print(sel)

#2 冒泡排序（随便站一列，让第一个学生往后比较，遇到大的再接力）
def bubbleSort(lyst):
    n=len(lyst)
    while n>1:
        i=1
        while i<n:
            if lyst[i]<lyst[i-1]:
                swap(lyst,i,i-1)
            i+=1
        n-=1
#bubbleSort(sel)        
#print(sel)

#3 快速排序之一
def partition(lyst,left,right):
    middle=(left+right)//2
    pivot=lyst[middle]
    lyst[middle]=lyst[right]
    lyst[right]=lyst[left]
    boundary=left
    for index in range(left,right):
        if lyst[index]<pivot:
            swap(lyst,index,boundary)
            boundary+=1
    swap(lyst,right,boundary)
    return boundary

#递归
def quickSortHelper(lyst,left,right):
    if left<right:
        pivotLocation=partition(lyst,left,right)
        quickSortHelper(lyst,left,pivotLocation-1)
        quickSortHelper(lyst,pivotLocation+1,right)

def quickSort(lyst):
    quickSortHelper(lyst,0,len(lyst)-1)

import random    
def main(size=7,sort=quickSort):
    lyst=[]
    for count in range(size):
        lyst.append(random.randint(1,size+1))
    print(lyst)
    sort(lyst)
    print(lyst)
        
#if __name__=="__main__":
    #main()
    
#4 快速排序之二
def quickSort2(myList,start,end):
    #判断low是否小于high,如果为false,直接返回
    if start < end:
        i,j = start,end
        #设置基准数
        base = myList[i]

        while i < j:
            #如果列表后边的数,比基准数大或相等,则前移一位直到有比基准数小的数出现
            while (i < j) and (myList[j] >= base):
                j = j - 1
            #如找到,则把第j个元素赋值给第个元素i,此时表中i,j个元素相等
            myList[i] = myList[j]
            #同样的方式比较前半区
            while (i < j) and (myList[i] <= base):
                i = i + 1
            myList[j] = myList[i]
        #做完第一轮比较之后,列表被分成了两个半区,并且i=j,需要将这个数设置回base
        myList[i] = base
        #递归前后半区
        quickSort2(myList, start, i - 1)
        quickSort2(myList, j + 1, end)
    return myList

#myList = [49,38,65,97,76,13,27,49]
#print("Quick Sort: ")
#quickSort2(myList,0,len(myList)-1)
#print(myList)

#归并排序
def merge_sort( li ):
    #不断递归调用自己一直到拆分成成单个元素的时候就返回这个元素，不再拆分了
    if len(li) == 1:
        return li

    #取拆分的中间位置
    mid = len(li) // 2
    #拆分过后左右两侧子串
    left = li[:mid]
    right = li[mid:]

    #对拆分过后的左右再拆分 一直到只有一个元素为止
    #最后一次递归时候ll和lr都会接到一个元素的列表
    # 最后一次递归之前的ll和rl会接收到排好序的子序列
    ll = merge_sort( left )
    rl =merge_sort( right )

    # 我们对返回的两个拆分结果进行排序后合并再返回正确顺序的子列表
    # 这里我们调用拎一个函数帮助我们按顺序合并ll和lr
    return merge(ll , rl)

#这里接收两个列表
def merge( left , right ):
    # 从两个有顺序的列表里边依次取数据比较后放入result
    # 每次我们分别拿出两个列表中最小的数比较，把较小的放入result
    result = []
    while len(left)>0 and len(right)>0 :
        #为了保持稳定性，当遇到相等的时候优先把左侧的数放进结果列表，因为left本来也是大数列中比较靠左的
        if left[0] <= right[0]:
            result.append( left.pop(0) )
        else:
            result.append( right.pop(0) )
    #while循环出来之后 说明其中一个数组没有数据了，我们把另一个数组添加到结果数组后面
    result += left
    result += right
    return result

if __name__ == '__main__':
    li = [49,38,65,97,76,13,27,49]
    li2 = merge_sort(li)
    print(li2)
    
    