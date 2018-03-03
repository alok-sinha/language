
import random



#
# Selecting m integers from 1,m, such that they are equally likely.
# If s number is to be selected from r numbers, select the next one with probablility s/r
# To generate s/r probability, generate a big random number and mod it with r. This gives us 
# number between [0,r-1], equally likely. If this number is less than s, then event has occured.
#
# If we generate a random number between 0,4, then probablilty that this oin [0,1] is 2/5, 
# or it is [3.4], or any other 2 set member will ne 2/5 probability
# 

selected = 0
remaining = 100

for i in range(0,remaining):
	r = random.randint(0,100) % remaining
	print r
	if (2 - selected) > r:
		print "Selecting ", i, " random = ", r
		selected += 1
	remaining -= 1


print random.randint(100,200)