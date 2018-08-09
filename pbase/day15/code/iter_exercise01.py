# iter_exercise_01.py

s = {'唐僧','悟空','八屆','沙僧'}
n = iter(s)
while True:
	try:
		print(next(n))
	except StopIteration :
		print("迭代中止")
		break