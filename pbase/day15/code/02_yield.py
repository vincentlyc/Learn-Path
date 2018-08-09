# 02_yield.py


#此示例示意生成器函數的定義及使用
def myyield():
	'''此函數為生成器'''
	print("即將生成2")
	yield 2
	print('即將生成3')
	yield 3
	print('即將生成5')
	yield 5
	print("myyield函數返回")

# 用 for 語句訪問 myyield函數

for x in myyield():
	print(x)
