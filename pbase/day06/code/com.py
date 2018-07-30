# x // f[1] + x // f[2] + ... + x // f[n] = x

# n = int(input("請輸入整數："))
L = []

for n in range(1,10) :
	for x in range(1, n) :
		if n % x == 0 :
			L.append(x)
			continue

if sum(L) == n :
	print(L)

else :
	print("該數不是完全數")