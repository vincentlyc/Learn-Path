

def div_apple(n):
	print ('%d個蘋果您想分給幾個人?' % n)
	s = input ('請輸入人數：')
	cnt = int(s) #<<= 可能觸發ValueError錯誤異常
	# 以下一行可能觸發ZeroDivisionError錯誤異常
	result = n/ cnt
	print('每人個分了', result, '個蘋果')


# 以下是調用者
# 我try-except語句來捕獲並處理ValueError類型的錯誤
try:
	print("開始分蘋果")
	div_apple(10)
	print("分蘋果完成")
except ValueError :
	print("錯誤以被捕獲")
except :
	print("除ValueError類型的錯誤外,其他錯誤都可以被捕獲")

print('程序正常退出')