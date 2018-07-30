

x = 1
g = {}
l = {}
while True:
	s = input("請輸入程序")
	if s == 'break' :
		break
	exec(s, g, l)

print(x)