
def myfun(a, b, c):
	print("a-->",a)
	print("b-->",b)
	print("c-->",c)


myfun(100, *(200, 300)) # 正確
myfun(*[100, 200], 300) # 正確
myfun(*[100], 222, *(300,))  #正確
myfun(100, c=333, b=222) #正確
myfun(c=333, b=222, 111)  #錯誤
myfun(100, *{"c" : 334, "b": 220}) #正確
myfun(**{"c" : 333, "a" : 111}, b = 222) #正確