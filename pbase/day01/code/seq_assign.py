 
#seq_assign.py

a = 10
b = 20

# a = 10
# b = 20
# a, b = 10, 20
# a, b = (10, 20)
a, b = [10, 20] #對的
# a, b = [10, 20, 30 ] #錯的
print(a, b) 

a, b = b ,a #將b---> a同時a --->b
print(a, b) #20 10