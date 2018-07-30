


#def myadd(x, y):
#	return x + y

#def mymul(x, y):
#	return x * y

def get_op(op):
	if op == "加":
		def myadd(x, y):
			return x + y
		return myadd
	elif op == '乘' :
		def mymul(x, y):
			return x * y

a = int(input("請輸入一個數"))
b = int(input("請輸入一個數"))
operator = input("請輸入操作方法:")
fn = get_op(operator)
print("結果是:", fn(a, b))
