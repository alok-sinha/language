#Binary search vs Unordered search in list
#
# Linear search is O(n) in search and insert
# Binary search is log(n) in search and O(n) for key insert. This is good if list is mostly static and pre-sorted.
# In practical applications where insert and search is intermixed, it is not good. 
# 
# How do we acheive log(n) for both insert and search?
# Binary search already has log(n) efficiency for earch. Idea is bring efficiency of insertion of linked list.
# 
# So we need a linked data structure.
#
# 1) BST:
#     Binary search relies on quickly moving to middle of data. So a recursive structure like BST helps!
#     Tree with random data leads to 2log(n) expected time. 	
# 
# 2) Hash table:
#

def bsearch(data, key):
    lower = 0
    higher = len(data)-1

    while lower <= higher:
        mid = (lower + higher)/2 

        print "Lower {0}, Higher {1}".format(lower, higher)

    	if data[mid] == key:
    		return mid
    	elif data[mid] > key:
    	    higher = mid-1
    	elif data[mid] < key:
    	    lower = mid+1

    	   	
    return -1

def bsearch_last_occur(data, key):
    lower = 0
    higher = len(data)-1
    result = -1

    while lower <= higher:
        mid = (lower + higher)/2 

        print "Lower {0}, Higher {1}".format(lower, higher)

    	if data[mid] == key:
    		result = mid
    		lower = mid+1
    		
    	elif data[mid] > key:
    	    higher = mid-1
    	
    	elif data[mid] < key:
    	    lower = mid+1

    	   	
    return result

def bsearch_first_occur(data, key):
    lower = 0
    higher = len(data)-1
    result = -1

    while lower <= higher:
        mid = (lower + higher)/2 

        print "Lower {0}, Higher {1}".format(lower, higher)

    	if data[mid] == key:
    		result = mid
    		higher = mid-1
    		
    	elif data[mid] > key:
    	    higher = mid-1
    	
    	elif data[mid] < key:
    	    lower = mid+1

    	   	
    return result


#
# Returns first key greater than a given key. The relies on fact that in case of
# unsuccessful search, lower points to element lesser than key, and next key is higher than key.
# Basically searched key lies between [low, low+1]
#
def bsearch_first_greater(data, key):
    lower = 0
    higher = len(data)-1
    result = -1

    while lower <= higher:
        mid = (lower + higher)/2 

        print "Lower {0}, Higher {1}".format(lower, higher)

    	if data[mid] == key:
    		result = mid
    		lower = mid+1
    		
    	elif data[mid] > key:
    	    higher = mid-1
    	
    	elif data[mid] < key:
    	    lower = mid+1

    if result == -1:
    	print "Not found"
    	print lower,":", higher
    	if d[lower] > key:
    		return d[lower]
    	else: 
            return d[lower+1]

    if result == len(data)-1:
    	print "Nothing greater than ", key
    
    else:
        return data[result +1]	


def BinarySearchRotated(nums):
    low = 0
    high = len(nums)-1

    while low < high:
        mid  = (low  + high)/2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid

    print high,nums[high] 




#
# This returns how many keys are there before the searched key
# Key idea is that "low" is pointing to key lower than "key". This is same 
# logic used in bsearch_first_greater to find first number greater than key.
#
#def bsearch_how_many_before_key ()


d = [1,1,2,5,7,9,10,10,10,24,34] 

#print bsearch_last_occur(d, 34)
#first,last =  bsearch_first_occur(d,10), bsearch_last_occur(d,10)
#print first, last 

print bsearch_first_greater(d,8)  

#d = [1,2,3,4,5,0]
#BinarySearchRotated(d)
