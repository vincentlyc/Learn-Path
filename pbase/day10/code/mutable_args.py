# mutable_args.py


L = [1,2,3]


def fn(x) :
	x = [4, 5, 6]
	

fn(L)
print(L)