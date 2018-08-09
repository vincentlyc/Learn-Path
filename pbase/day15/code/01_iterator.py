# 01_iterator.py

# 用for 語句訪問可迭代對象L
L = [2,3,5,7]
for x in L:
	print (x)

print('--------以下是while語句訪問L-------')
#用while循環語句來訪問如下列表
it = iter(L) # 用L來生成一個迭代器
while True:
	try:
		x = next(it)
		print(x)
	except StopIteration
		print("迭代中止")
		break