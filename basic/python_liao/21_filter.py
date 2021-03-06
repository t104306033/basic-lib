# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 19:20:32 2017

@author: VX
"""

#==============================================================================
# filter(過濾器)
#==============================================================================
# 以傳入的boolean function作為條件函式，蒐集所有符合條件的元素到一個list當中。
def fn(x):
  return x if x > 5 else None

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = filter(fn, a)
print(list(b))

# 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))) # [1, 5, 9, 15]

# 把一个序列中的空字符串删掉，可以这么写
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))) # ['A', 'B', 'C']

# 用filter求素数
'''
计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单
首先，列出从2开始的所有自然数，构造一个序列
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉
3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉
5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
取新序列的第一个数5，然后用5把序列的5的倍数筛掉
7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
不断筛下去，就可以得到所有的素数。
用Python来实现这个算法，可以先构造一个从3开始的奇数序列
'''
# 注意这是一个生成器，并且是一个无限序列。
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

# 然后定义一个筛选函数
def _not_divisible(n):
    return lambda x: x % n > 0

# 最后，定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
'''
这个生成器先返回第一个素数2，然后，
利用filter()不断产生筛选后的新的序列
由于primes()也是一个无限序列，
所以调用时需要设置一个退出循环的条件
'''
for n in primes():
    if n < 100:
        print(n)
    else:
        break
    
del (a, n)
'''
注意到Iterator是惰性计算的序列，
所以我们可以用Python表示“全体自然数”，
“全体素数”这样的序列，而代码非常简洁。
'''

'''练习
回数是指从左向右读和从右向左读都是一样的数，
例如12321，909。
请利用filter()滤掉非回数
'''

# -*- coding: utf-8 -*-

def is_palindrome(n):
    n = str(n)
    a = 0
    for i in range(len(n)):
       a = int(n[i]) * 10 ** i + a
    return int(n) == a

# 测试:
output = filter(is_palindrome, range(1, 1000))
print(list(output))


