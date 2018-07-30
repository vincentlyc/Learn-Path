# 04_sys_exit.py


def f():
	print("f程序開始調用")
	import sys
	sys.exit(0)
	print('f()結束調用')

f()
print('程序結束')