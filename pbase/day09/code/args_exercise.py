# args_exercise.py

#def mixmax(*args) :
#	print("maxnumer:",max(args), "minnumber:",min(args))

#mixmax(23,21,3223,3,43,123)

def minmax(*t) :
	if len(t) < 2 :
		print("at least 2 argument")
	min_v = t[0]
	for i in range(1, len(t)) :
		if min_v < t[i] :
			min_v = t[i]

	max_v = t[0]
	for i in range(1, len(t)) :
		if max_v > t[i] :
			max_v = t[i]

	return (min_v, max_v)

x, y = minmax(20,8,31,2,23)

print('smallest number:',x)
print('bigest number:',y)
