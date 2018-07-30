
def sum(n):
	sum0 = 0
	for i in range(0,n+1) :
		sum0 = sum0 + i
	return sum0

#print(sum(100))

def myfac(n):
	a = 1
	for i in range(1,n+1) :
		a = a * i
	return a

#print(myfac(100))

def sq(n):
	sum0 = 0
	for i in range(1,n+1) :
		sum0 = sum0 + i ** i
	return sum0

print(sq(3))

