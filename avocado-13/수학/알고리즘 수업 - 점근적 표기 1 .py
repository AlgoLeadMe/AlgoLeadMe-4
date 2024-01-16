import math
import sys

input = sys.stdin.readline

a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
res = 1

def h(n):
    global a1
    global a0
    global c
    return (a1-c)*n + a0
n = n0 

if(a1<=c) and h(n0)<= 0 :
    res = 1
else:
    res = 0 
print(res)