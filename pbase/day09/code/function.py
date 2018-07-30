# function.py

def say_hello():
	print("hello world!")
	print("hello tarena")
	print("hello everybody")


def mysum(a,b):
	print("調用 mysum(%s, %s)" % (a, b))
	sum2 = a + b

say_hello()
say_hello()
mysum(100, 200)
mysum(300, 400)
# print(sum2) #出錯,sum2不存在