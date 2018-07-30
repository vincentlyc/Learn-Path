# pri.py

primes = []
while True :
	n = int(input("請輸入大於0的整數"))
	if n <= 1:
		break  #中止循環

	for x in range(2, n) :
		if n % x == 0 :
			break　　#不是質數
	else :
		print(x+1, "是質數!")
		primes.append(n)

print("所有質數", primes)