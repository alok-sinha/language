
import random
#from random import *


def partitionWithEqual(A, start, end):
    
    pi = random.randint(start, end)
    A[pi], A[end] = A[end], A[pi]

    pivot = A[end]
    b = 0
    eq = None
    i = start
    while i < end:
        if A[i] < pivot:
            if eq != None:
                A[eq] = A[i]
                eq += 1
                A[b], A[i] = pivot, A[b]
                b += 1
            else:
                A[i], A[b] = A[b], A[i]
                b += 1
        elif A[i] == pivot:
            A[i], A[b] = A[b], A[i]
            if eq == None:
                eq = b
            b += 1    

        i += 1
             
    A[end],A[b] =  A[b],A[end]    
    if eq == None:
        eq = b
    b += 1
  
    return b,eq     

def findkSmallest(A,start, end,k):
    m,e = partitionWithEqual(A, start, end)
    if k >= e and k < m:
        return A[e]
    elif k < e:    
        return findkSmallest(A, start, e-1,k)
    else:
        return findkSmallest(A, m, end, k-m)        





A = [1,8,5,3,10,4,5]
#A = [5,5,5,5]
print partitionWithEqual(A, 0, len(A)-1)
print findkSmallest(A, 0, len(A)-1, 1)

                

def partition(nums, start, end):


    pi = random.randint(start, end)
    print start, end, pi
    nums[pi], nums[end] = nums[end], nums[pi]

    #pi = random.randint(0,len(nums)-1)
    #pi = end
    i = start
    b = start
    pivot = nums[end]
    #nums[pi], nums[n-1] = nums[n-1], nums[pi]

    while i < end:
        if nums[i] < pivot:
           nums[i], nums[b] =  nums[b],nums[i]
           b += 1
        i += 1   
    nums[end],nums[b] = nums[b],nums[end]

    #print nums,b
    print nums, start, end, b, pivot
    return b

def quicksort(A, i,j):

    if i < j:
        index = partition(A, i,j)
    
        quicksort(A, i, index-1)
        quicksort(A, index+1, j)


l = [8, 11, 18, 1, 6, 15, 14, 9, 15, 12, 16, 5, 0, 15, 2, 7, 4, 19, 3, 10]
quicksort(l, 0, len(l)-1) 
#quicksort([5,5,5,5], 0, 3)
#print l
#print partition([30,20])  
print partitionWithEqual(l, 0, len(l)-1)
           



