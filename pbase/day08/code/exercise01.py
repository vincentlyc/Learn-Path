#集合練習：
maner = set(["曹操","劉備","周瑜"])
worker = set(["曹操","周瑜","張飛","趙雲"])

print(maner & worker)
print(maner - worker)
print(worker - maner)
print()
print(maner ^ worker)
print(len(maner)+len(worker))