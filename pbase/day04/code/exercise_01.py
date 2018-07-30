 
 # homework.py

n = 0
while n <= 20:
	print(n)
	n += 2

y = 1
while y <= 20:
	print(y)
	y += 2 

else:
	print("循環結束")

x = 1
while x <= 10:
	print(x, end =' ')
	x += 1 

else:
	print("循環結束")


y = 65
while y <= 90:
	print(chr(y), end ='')
	y += 1 

else:
	print("循環結束")

y = 65
x = 97
while y <= 90 and x <= 122:
	print(chr(y),chr(x),end = "")
	y += 1
	x += 1


else:
	print("循環結束")