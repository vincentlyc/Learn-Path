# dict_args.py

def myfun(**kwargs) :
	print("參數個數",len(kwargs))
	for k, v in kwargs.items():
		print(k,"-->",v)

myfun(name="tarena", age=15) 
myfun(a=11, b="FUCK",d="n32", e=15)