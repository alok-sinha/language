

def func(i):
	for j in i:
		yield j

x = func(range(5))
print next(x)
print next(x)
print next(x)

	