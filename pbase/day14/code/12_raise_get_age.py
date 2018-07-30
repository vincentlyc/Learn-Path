# 12_raise_get_age.py


# 此示例示意用raise發出錯誤通知給調用者
# 甲寫了寒數 get_age

def get_age():
	s = int(input("請輸入年齡(0~140)"))
	if 0 <= a <= 140:
		return a
	if a > 140:
		raise OverflowError("人的年齡不可能大於140")


# 乙用戶調用get_age()
try:
	age = get_age()
except ValueError as err:
	print("用戶輸入的不是數,以做出相對處裡")
	age = 0
except OverflowError as err:
	print("用戶輸入年齡過大")
	age = 0

print('得到年齡的', age)

