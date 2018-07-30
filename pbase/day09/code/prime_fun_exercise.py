# prime_fun_exercise.py


#K = int(input("請輸入："))

def isprime(x):
    if x <= 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True


n = int(input("起始值："))
m = int(input("結束值："))
#############################

L = []
for x in range(n, m+1):
    if isprime(x) == True:
        L.append(x)
        continue

print(L)

#############################


def prime_n2m(n, m):
    L = []
    for x in range(n, m+1):
        if isprime(x) == True:
            L.append(x)
    return L


L = prime_n2m(5, 19)
print(L)

#############################


def primes(n):
    return prime_n2m(1, n)


L = primes(130)
print(L)
