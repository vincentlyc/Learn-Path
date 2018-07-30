# 11_raise.py

# 此示例示意用raise語句來發出異常通知
# 供try - except 語句來捕獲

def make_except():
	print("開始...")
	# raise ZeroDivisionError #手動發生一個錯誤通知
	e = ZeroDivisionError
	raise e #觸發e綁定錯誤
	print("結束")



try:
	make_except()
	print("make_except調用完畢！")
except ZeroDivisionError as err:
	print("出現零除錯誤,處理並轉為正常狀態")
	print('err綁定的對象是:',err )