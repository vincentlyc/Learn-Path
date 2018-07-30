# homework.py


info = {}
nlist = []
alist = []

for x in range(4) :
	for i in range(4) :
		name = str(input("請輸入學生姓名："))
		age = int(input("請輸入學生年齡:"))
		nlist.append(name)
		alist.append(age)
		break

info = {nlist[y] : alist[y] for y in range(4)}
print(info)

for k,v in info.items():
	print(k,v)

print("""+----------+----------+""")
print("""|   姓名   |   年齡   |""")
print("""+----------+--------- +""")

#for i in info.key():
#	break
#for k in info.values():
#	break
#print (i ,k)