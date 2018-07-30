m = int(input("請輸入開始數："))
n = int(input("請輸入結束數："))
L = []
L2 = []


def prime_m2n(m,n):
	for i in range(m, n+1) :
		L.append(i)
		continue

	for g in L:
		for k in range(2, L[-1]):
			if g % k == 0 :
				L.remove(g)
				break
			else:
				break
	print(L) 
prime_m2n(m,n)
