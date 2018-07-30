# homework6.py

#方法1

a = 1
b = 1
print(a, end = ' ')
print(b, end = ' ')

for i in range(18) :
	n = a + b
	print(n, end = ' ')
	a = b
	b = n

#方法2

a = 1
b = 1
print(a, end = ' ')
print(b, end = ' ')

for i in range(18) :
	print(a + b, end = ' ')
	a, b = b, a + b

#方法3

a = 1
b = 1

for i in range(20) :
	print(a end = ' ')
	a, b = b, a + b