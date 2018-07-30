# break2.py


i = 0
while i < 2 :
	j = 8
	while (j < 100):
	    print(i, j)
	    if j >= 10 :
	    	break ;
	    j += 1
	i += 1
else :
	 print ("while循環結束")

print("程序結束")