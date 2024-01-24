import sys
import math

""" Entrée 27

Sortie
7
11
17
19
23
"""

def f(n, m={}):
    if n in m:
        return m[n]
    if n <= 2:
        return 1
    m[n] = f(n-1, m) + f(n-2, m)
    return m[n]
n = int(input())
l=[f(i)for i in range(3 , n) if f(i)<=n]

for i in range(2,n+1):
    if all(i%j for j in l):
        print(i)