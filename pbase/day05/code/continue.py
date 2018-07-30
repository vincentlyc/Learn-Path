
# continue.py

# 打印10以內的偶數
for x in range(10):
    # 如果是基數則跳過打印
    if x % 2 == 1 :
    	continue
    print(x) # x 一定是偶數
else:
    print("打印結束")