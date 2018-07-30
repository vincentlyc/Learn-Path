
v = 100


def fn ():
	v = 200  
	global v  #錯的

fn()
print(v)