# 05_test_mymod1.py



# 此程序用於示意導入"小張"寫的模塊mymod1
# 並調用相應的數據和函數

import mymod1
mymod1.myfun1()
print(mymod1.name1) #audi

from mymod1 import name2
print("mymod1裡的name2為：", name2)


from mymod1 import *
myfun2()