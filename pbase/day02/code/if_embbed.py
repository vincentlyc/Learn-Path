
score = input("請輸入學生的成績：")
score = int(score)

if 0 <= score <= 100:
	print("成績合法")
	if score < 60:
		print("不及格")
	elif score < 80:
		print("及格")
	elif score < 90:
		print("優秀")
	elif score < 100:
		print("你作弊")	

else:
	print("成績不合法")

print("程序退出！")