# 步长，计数，结束
for i in range(2, 27, 4):
    print(i, end=',')


# 素数
import math
def isprime(num):
    if num <= 1:
        return False
    # for i in range(2, int(math.sqrt(num)) + 1):  
    #     if num % i == 0:  
    #         return False 
    i = 2
    while i*i <= num:
        if num % i == 0: # i是num的质数
            return False
        i += 1
    return True

# 约数
def getfactors(num):
    factors = []
    factors.append(0)
    for i in range(1, int(num) + 1):
        if num % i == 0: # i是num的约数
            factors.append(i)
    return factors

refactor = getfactors(12)
print(refactor)

# 素因子分解
def primefactors(n):
    pflist = []
    while 1 != n:
        for i in range(2, int(n) + 1):
            if 0 == n % i:
                pflist.append(i)
                n = n // i
                break
    # for j in range(len(pflist)):
    print(pflist)
primefactors(90)

# 完全数
def isperfect(num):
    factors = []
    for i in range(1, int(num) + 1):
        if num % i == 0:
            factors.append(i)
    len_factors = len(factors)
    total = 0
    for j in range(len_factors - 1):
        total += factors[j]
    if(num == total):
        return 1
    else:
        return 0  
tag = isperfect(6)
print(tag)

# 阶乘
def factorial(num):
    newnum = 1
    for i in range(1, num + 1):
        newnum *= i
    return newnum
print(factorial(4))

import math
num = input('请输入一个数字：')
print(math.factorial(num))

# 斐波那契数列
def fibonacci(num):
    a, b = 0, 1
    templist = []
    for i in range(num):
        a, b = b, a+b
        templist.append(a)
    print(templist[-1])

fibonacci(6)
