


def powerset(A, k, positions, ps):
	def printSet(A, positions):
		tmp = [A[i] for i in range(len(positions)) if positions[i] == True]
		ps.append(list(tmp))

	if k == len(positions):
		printSet(A, positions)
		return

	for t in (True, False):
		positions[k] = t
		powerset(A, k+1, positions, ps)
		positions[k] = False


l = [1,2,3]
ps = []
powerset(l, 0, [False]*len(l), ps)
print ps, len(ps)

