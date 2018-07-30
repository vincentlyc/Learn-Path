
text = input("請輸入月份？")
month = int(text)

if 1 <= month <= 3:
     print("春季")
elif 4 <= month <= 6:
     print("夏")
elif 7 <= month <= 9:
     print("秋")   
elif 10 <= month <= 12: 
     print("冬")

else:
   print("成績不合法")

print("結束")

