# guess.game.py

import random

def guess() :
	gs = int(random.randrange(0,101))
	return gs

x = guess()
times = 0

while True :
	y = int(input("請輸入:"))
	times += 1

	if y > x :
		print("您猜的數字比較大")

	elif y < x :
		print("您猜的數字比較小")

	elif y == x :
		print("恭喜你猜對了")
		break

print("您猜了共%d次" % times)