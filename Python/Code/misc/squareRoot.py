


def sqrt(n):
	l = 1.0
	h = n
	m = (l + h)/2
	count = 0
	while abs(m*m - n) > (0.001*n):
		print m
		if m*m > n:
			h = m
		else:
			l = m
		m = (l + h)/2	

		count += 1
		if count == 100:
			break	

	print m

sqrt(5)				