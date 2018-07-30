#dict_args_ex.py

def teatime(**kwargs) :
	for k, v in kwargs.items():
		print('my desert is', k,',', 'drink is', v)

teatime(macaron = 'coffe', brownie = 'milktea', sandwich = 'blacktea')
