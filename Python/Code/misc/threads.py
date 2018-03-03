import concurrent.futures


import os, time
def counter( count): # run in new process 
	for i in range( count): 
		time.sleep( 1) # simulate real work 
		print('[% s] = > %s' % (os.getpid(), i))

"""totalForks = 0
for i in range(5):
	totalForks += 1
	pid = os.fork()

	if pid == 0:
		counter(5)
		os._exit(0)
	else:
		print "In pranet, process spwaneed ", pid	

print "Total forks",totalForks
"""

def task(arg1, arg2, arg3):
	print "Task with ags : ", arg1, arg2, arg3


threads = concurrent.futures.ProcessPoolExecutor(max_workers = 10)

for i in range(1,20):
	threads.submit(task, i+1,i+2,i+3)


