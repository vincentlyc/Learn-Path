# global_var.py

v = 100      #<<<--此為全局變量

def fn():
	v = 200  #<<<--此為局部變量
	print(v)

fn() # 200
print(v)  #100