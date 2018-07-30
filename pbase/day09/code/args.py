# args.py

def my fun(a, b, c):
	print("a-->",a)
	print("b-->",b)
	print("c-->",c)

# 位置傳參：
myfun(100, 200, 300)

# 序列傳參：
s1 = [11, 22, 33]
myfun(*s1)  # 等同於 myfun(s1[0], s1[1], s1[2])

s2 = (1.1, 2.2, 3.3)
myfun(*s2)

s3 = "ABC"  # 字符串

