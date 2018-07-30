
# mymod5.py

'''此模塊示意_name_數性的作用
'''


def f1():
    print('f1被調用')


if __name__ == '__main__':
    print("mymod5.py正在當作主模塊運行")
    f1()
else:
    print("mymod5.py正在被其他模塊導入")
    print("模塊名為：", __name__)
