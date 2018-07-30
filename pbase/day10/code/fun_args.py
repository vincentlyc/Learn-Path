
def tab(x, y) :
	return "|" + x.center(13) + \
	'|' + y.center(13) + "|"

def string(x, y) :
	return "姓名" + x + "年齡：" + y

def myprint(fx, x, y) :
	s = fx(x, y)
	print(s)

myprint(tab, "tarena", "15")
myprint(tab, "小張", "18")
