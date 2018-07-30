
# day02_pratice2.py

m = int(input("請輸入數學成績"))
c = int(input("請輸入國文成績"))
e = int(input("請輸入英文成績"))

if m > e >= c:
	print (m, c, round(( m+ e+ c)/3,1))
elif m > c >= e:
    print (m, e, round(( m+ e+ c)/3,1))

elif c > m >= e:
    print (c, e, round(( m+ e+ c)/3,1))
elif c > e >= m:
    print (c, m, round(( m+ e+ c)/3,1))

elif e > c >= m:
    print (e, m, round(( m+ e+ c)/3,1))
elif e > m >= c:
    print (e, c, round(( m+ e+ c)/3,1))