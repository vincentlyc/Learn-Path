

def div_apple(n):
	print ('%d個蘋果您想分給幾個人?' % n)
	s = input ('請輸入人數：')
	
	try :
		cnt = int(s) #<<= 可能觸發ValueError錯誤異常
	# 以下一行可能觸發ZeroDivisionError錯誤異常
		result = n/ cnt
		print("每人分了", result,"蘋果")
	except ZeroDivisionError:
		print("被零除錯誤")


try:
	print("開始分蘋果")
	div_apple(10)
	print("分蘋果完成")
except ValueError:
	print("值錯誤已處裡")
else:
	print("此try語句沒有進入異常")
finally:
	print("我是finally子句,我一定會執行")

print('程序正常退出')