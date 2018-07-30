
# day02_pratice1

km = float(input("請輸入公里數"))

# 1.if km <15,price = 13
# 2.if km price = 13 + km*2.3
# 3.price = 13 + km*2.3 + price*0.5

price = 13 if km < 3.5 else 13 + km*2.3

print(round(price if km <= 15 else price + km*2.3*0.5,1),"元")
