
# 3. 當有兩層或兩層以上函數嵌套時,訪問nonlocl變量只對最近一層的變量進行操作

def f1():
	v = 200
	def f2():
		v = 300
		def f3():
			nonlocal v
			v = 400
		f3()
		print('f2.v=', v)
	f2()
	print('f1.v=',v)

f1()
