# return_fn.py

def getfn() :
		def print_hello():
				print("hello")
		return print_hello  #print_hello()  # print('hello')

fn = getfn()
print(fn)
fn()
# fn()