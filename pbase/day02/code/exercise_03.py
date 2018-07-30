

text1 = input("請輸入現在幾時：")
hour  = int(text1)

text2 = input("請輸入現在幾分：")
minute= int(text2)

text3 = input("請輸入現在幾秒：")
sec   = int(text3)

time_pass = hour * (60**2) + minute * 60 + sec
print( "現在已經過了", time_pass,"秒")

