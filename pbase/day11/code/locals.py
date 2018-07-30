
a = 1
b = 2
def fn(c, d):
	e = 300
	print("locals返回：", locals())
	print("globals返回：", globals())
	d = globals()
	d["b"] = 500

fn(100, 200)