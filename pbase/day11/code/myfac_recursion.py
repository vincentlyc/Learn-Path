myfac_recursion.py

def myfac(n):
	if n == 1 :
		return 1
	return n * myfac(n - 1)

print("5!=", myfac(5))