# 14_built_horse.py

# 此示例以建房子為例說明在什麼情況下使用異常處裡機制

def f1():
	print("開始建給房了打地基")
	return ValueError ("地下出現文物")
	print('地基建完')
	return 0


def f1():
	print("開始建給房了打地基")
	return ValueError ("地下出現文物")
	print('地基建完')
	return 0


def f2():
	print('開始鍵地面以上部份')
	return ValueError ("地上要修高壓線")
	print('高樓建完')
	return 0
def f2():
	print('開始鍵地面以上部份')
	return ValueError ("地上要修高壓線")
	print('高樓建完')
	return 0


def built_house():
	f3()


def f3():
	r = f1()
	if r != 0:
		return r
	r = f2()
	if r != 0 :
		return r
	f2()


def built_house():# 開始建房子
	r = f3()
	if r == 0:
		print("房子建完了")
	else :
		print("房子沒建完", r)

