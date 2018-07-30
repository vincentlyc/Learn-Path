# print.py

print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='' )
print(1, 2, 3, 4, sep='-')
print(1, 2, 3, 4, sep='#')
print("我是第一行漢", end="\n\n\n")
print("我是第二行漢字")

print("我可能會放在緩衝區", end='')

import time
time.sleep(10)
print("我睡醒了")

# text = input("請輸入回車鍵繼續")
print('a', end='')
print('b', end='')
print('c', end='')
print('d', end='')
print()  #輸出換行'\n'