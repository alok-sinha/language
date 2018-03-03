
from collections import *
o = OrderedDict()
o[1] = 10
o[4] = 40
o[3] = 30
o[2] = 20
o[0] = 0

print o
o.pop(3)
o[3] = 30
print o.keys()
for key in o:
	print key

o.pop(o.keys()[0])
print o	