
def deco(fn):
    print("裝飾器函數被調用, 並返回原函數")
    print(fn)
    return lambda : print("hello world")

@deco
def myfunc():
    print("函數myfunc被調用！")

# 以上@deco等同於此語句
# myfunc = deco(myfunc)

myfunc()
myfunc()