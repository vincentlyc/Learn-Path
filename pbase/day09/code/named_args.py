# named_args.py

def myfun1(a, b,*, c) :   #c 為命名關鍵字形參
	print(a, b, c)


myfun1(1,2, c=3) #對的
myfun1(11, 22, 33)  ＃錯的

def mysum2(a, *args, b, c) :  #b,c為命名關鍵字形參
	print(a,b,c, args)

myfun2(1, 2, 3, 4)  #錯的
myfun1(1, 2, b=3, c=4) #對的
myfun1(11, c=44, b = 33)
 