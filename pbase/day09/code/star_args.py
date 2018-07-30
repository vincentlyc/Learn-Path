# star_args.py

def myfun(*args):
	print("實參個數是", len(args))
	print(args)
	i = 1
	for x in args:
		print("第",i ,"個參數是：", x)
		i += 1


myfun(1,2)
print('-----------------------------')

myfun("100",200,"Three", 4.4)

