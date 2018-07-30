# deepcopy.py

import copy # 導入copy模塊
L = [20, 21, 22]
L1 = [10, L ,30]
L2 = copy.deepcopy(L1)	# 調用深拷貝函數進行複製
L[2] = 25
print(L1)	#[10, [20, 21, 25], 30]
print(L2)   #[10, [20, 21, 22], 30]
