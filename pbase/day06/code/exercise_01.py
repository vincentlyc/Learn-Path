# d6_exercise.py


x = int(input("請輸入第一個數："))
y = int(input("請輸入第二個數："))
z = int(input("請輸入第三個數："))

L = [x, y, z]
print("最大", max(L), "最小",min(L), "和", sum(L), sum(L) // len(L))