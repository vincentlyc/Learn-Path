
score = input("請輸入學生的成績") or "0"

score = int(score)

if score < 0 or score > 100:
	print("您輸入的不合法")
else:
	print("您輸入的是", score)