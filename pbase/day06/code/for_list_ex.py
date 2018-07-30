# for_list_ex.py

L1 = ['a','b','c','d','e']
L2 = ['A','B','C','D','E']

for i in L2 :
	for j in L1 :
		print(i,j,sep = '', end = ' ')
	print(end = '\n')
