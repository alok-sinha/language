


def fillSudoku(sudo):


	def findPossibleValuesToFill(i,j):
		r = sudo["row"][i]
		valuesFromRow = {x for x in range(1,10) if x not in r}

		c = sudo["column"][i]
		valuesFromColumn = {x for x in range(1,10) if x not in r}

		gr = calculateGridNo(i,j)
		g = sudo["grid"][gr]
		valuesFromGrid = {x for x in range(1,10) if x not in list(x for y in g for x in y)}

		return valuesFromRow & valuesFromColumn &  valuesFromGrid


	def findNextCellToFll():
		#Check row
		
		




		

	i,j = findNextCellToFll(sudo)
	if i == -1:
		return 0

	possibleValues = findPossibleValuesToFill(i, j)
	for value in possibleValues:
		sudo[i][j] = value
		if fillSudoku(sudo) == 0:
			return 0
		sudo[i][j] = 0

	return 1

sudo = {
	"row": [[0]*9]*9,
	"column": [[0]*9]*9,
	"grid" : [[[0 for i in range(3)] for j in range(3)] for k in range(9)]
	"gridCount" : [0]*9,
	"rowCount":[0]*9,
	"colCount" :[0]*9,
}	
			