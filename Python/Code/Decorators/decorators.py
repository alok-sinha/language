
def myDeco(function):
	def wrapper():
		print("This is before")
		function()
		print("This is after")
	return wrapper


@myDeco
def myFunc():
	print("From func")

myFunc = myDeco(myFunc)
myFunc()

