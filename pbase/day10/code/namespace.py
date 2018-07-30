
# namespace.py

v = 100  #全局變量 G

def fun1():
	v = 200  # 外部嵌套作用域 E
	print("fun1.v=",v)
	def fun2():
		v = 300   #局部變量 L
		print("fun2.v=",v)
	fun2()

fun1()
print("v=",v)