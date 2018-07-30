# 01_get_score.py

def get_score():
	try:
		x = input("請輸入成績：")
	except ValueError :
		return 0

	if 0<=x<=100
		return x # 用戶把正確輸入返回回去
	return 0

score = get_score
print('學生的成績是', score)