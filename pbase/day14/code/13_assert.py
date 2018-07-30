# 13_assert.py


# 使示例示意assert語句 的用法
def get_age():
	a = int(input("請輸入年齡"))
	# 以下語句會在a不在 [0,140]時觸發AssertionError錯誤
	assert 0 <= a <= 140, '年齡不再合法的範圍內'
	return a


try :
	age = get_age()
except AssertionError as e:
	print("錯誤原因是", e)
	age = 0
print('年齡是：', age)
