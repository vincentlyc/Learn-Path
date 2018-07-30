ex2.py

def mypower(x) :
	return sum(map(pow, range(1, x+1), range(x, 0, -1)
					)
				)

print(mypower(9))