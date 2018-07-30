
# Nar.py

for s in range(100, 1001) :
    b = s // 100
    c = s % 100 // 10
    g = s % 100 % 10
    s = b * 100 + c * 10 + g
    if b ** 3 + c ** 3 + g ** 3 == s :
        print(s, end = ' ' )

for s in range(100, 1001) :
	n = str(s)
	b = int(n[0])
	c = int(n[1])
	g = int(n[2])
	if s == b ** 3 + s ** 3 + g ** 3 :
	    print(x, end = '')

for b in range(0 , 10) :
    for c in range(0, 10) :