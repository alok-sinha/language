

class rec:
	name = "Alok"
	age = 40

	def __init__(self, name1):
		self.name1 = name1
	
	def __str__(self):
		print "called str"
		return "Printing str"

	def __repr__(self):
		print "Called repr"
		return "Printing using repr"	


x = rec("Kumar")

rec.name = "Sinha"
print "name1" in x.__dict__
print x.name	
#print x.__dict__["name"]	

print x
