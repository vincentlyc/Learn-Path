
text = input ("請輸入1~4季度")
n = int(text)

if n == 1:
	print("1,2,3")

elif n == 2 :
    print("4,5,6")

elif n == 3 :
    print("7,8,9")

elif n == 4 :
    print("10,11,12")

elif 0 > n: 
    print("輸入錯誤")
    
elif n > 4: 
    print("輸入錯誤")

print("程序結束")