# 給出一個數n,寫一個函數計算1+2**2+3**3....+n**n

# 方法1:
def mysum(n)
	def power(x)
		# return x**x
		return pow(x, x)
	mit = map(power, range(1,n+1))
	return sum(mit)



print(mysum(10))

# 方法2:
def mysum1(n):
	return sum(
		map(pow, range(1, n+1), range(1, n+1))
		)

print(mysum1(10))


# 分法3:
def mysum(n) :
	return sum(map(lambda x: pow(x,x), 
					range(1,n+1)))
