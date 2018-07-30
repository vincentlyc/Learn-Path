# return_exercise.py

a = int(input("please enter a number,x:"))
b = int(input("please enter a number,y:"))
c = int(input("please enter a number,z:"))


def sum3(a,b,c) :
	return a + b + c


def pow3(x) :
	return x**3


s = sum3(a,b,c)


print("三數總和：",s)
print("三數三次方總和：",pow3(a)+pow3(b)+pow3(c))
print("三數總和三次方：",int(s)**3)
