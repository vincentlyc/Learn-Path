# ex1
# ====================================================
def isprime(n):
	for i in range(2,n):
		if n % i == 0 :
			return False
	else :
		return True

L = [n for n in filter(isprime , range(1,101))]

# ex2
# ====================================================
def mysum(n) :
	if n == 1:
		return 1
	return(n + mysum(n-1))

mysum(5)

# ex3
# ====================================================



# ex4
# ====================================================