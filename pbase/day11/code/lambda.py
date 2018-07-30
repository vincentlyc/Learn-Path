
#myway
lambda x, y: max(x,y)

print((lambda x,y :max(x,y))(200,300))

#way1
def mymax(x,y):
	return x if x > y else y

mymax2 = lambda x, y :x if x > y else y

print(mymax2(100,200))

#way2
def mymax(x,y):
	return max(x,y)