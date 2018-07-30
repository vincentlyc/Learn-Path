# test.py

n = str("*")
star = int(input("請輸入整數"))

for y in range(1, star * 2 + 1, 2) :
	x = y * n
	s = x
	print( s.center(star * 2 + 1))

for z in range(0, star) :
	for z in n :
		print( n.center(star * 2 + 1))
