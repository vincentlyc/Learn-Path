# return.py

def fun1():
	print("fun1 is used")
	return 123
	print("this fun1 final row") # will not print, its end.

r = fun1()
print(r) # None

# max(a,b,c)

def fun2():
	return
	print("此行不會打印")


r = fun2()
print('r =',r)

def fun3():
	# return 123
	return[1,2,3]


x, y, z = fun3()
print(x, y, z)
