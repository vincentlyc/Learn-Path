# mymod7.py

'''此模塊示意模塊內的隱藏屬性'''



def f1():
	pass

def _f2():
	'''
	此函數在被其他模塊用 form import * 時不被導入
	'''
	pass

var1 = '變量1'
_var2 = '變量2'  #_var2也是隱藏變, 也不會被導入