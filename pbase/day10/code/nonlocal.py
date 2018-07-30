
var = 100


def outter():
	var = 200
	def inner():
		nonlocal var # 指定var為外層嵌套函數作用域
		var += 1 # 此行會出錯
		print("inner.var", var)
	inner()
	print("outter.var=", var)


outter()