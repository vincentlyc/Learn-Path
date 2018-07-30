# 10_try_finally.py


# 以煎蛋為例,
	# 1. 打開天燃
	# 2. 煎蛋
	# 3. 關閉天然氣

def fry_egg():
	print("打開天燃器點燃...")
	try:
	count = int(input("請輸入煎蛋個數："))
	print("煎蛋完成,共煎了%d個雞蛋" % count)
	finally:
	print("關閉天然氣")

try:
	fry_egg()
except :
	print("程序轉為正常狀態")