# 01_myhello.py

import sys


if sys.version[0] == '2' :
	print("我運行在python2裡")
elif sys.version[0] == '3':
	print("我運行在python3裡")

if sys.version_info[0] == 2:
	print("python2")
elif sys.version_info[0] == 3:
	print("python3")

print("當前的主版本號是：", sys.version_info.major,
	  "當前的次版本號是：", sys.version_info.major,
	  "當前的微版本號是：", sys.version_info.major)