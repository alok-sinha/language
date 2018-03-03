


def multiply(a,b):
	result = 0
	outerShift = 1
	for i in range(len(a)-1, -1, -1):
		innerShift = 1
		for j in range(len(b)-1, -1, -1):
			result += a[i]*b[j]*outerShift*innerShift
			innerShift *= 10
		outerShift *= 10

	print result


multiply([int(d) for d in str(3141592653589793238462643383279502884197169399375105820974944592)], [int(d) for d in str(2718281828459045235360287471352662497757247093699959574966967627)])			

