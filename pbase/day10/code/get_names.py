
#方法一
###############################################################
def get_names(x = []) :
	L = []
	while True:
		name = input("請輸入學生姓名:")
		if not name:
			break
		L.append(name)
	x.extend(L) # 追加列表
	x[:] = L    # 切片賦值
	return L

names = get_names()
print(names)


# 方式2
###############################################################
def get_names(L = []) :
	while True:
		name = input("請輸入學生姓名:")
		if not name:
			break
		L.append(name)	
	return L

n = []
get_names(n)
print(n)

