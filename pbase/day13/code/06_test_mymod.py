06_test_mymod.py


#此示示例示意個模塊內的變量不衝突

import mymod1
import mymod2

print('mymod1.name1 =', mymod1.name1)
print('mymod2.name1 =', mymod1.name2)

# 以下方法使用會引起變量衝突
from mymod1 import *
from mymod2 import *

print(name1)  # 已經發生衝突
