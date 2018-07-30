# mygame/games/contra.py


def play():
	print("正在玩contra")

print('contra 模塊被加載')

def gameover():
	# 用絕對路徑的方式導入
	# from mypack.menu import show_menu
	# 用相對導入
	from ..menu import show_menu
	show_menu()

	from mypack.games.tanks import play
	# from ...mypack.games.tanks import play 出錯...

	play()