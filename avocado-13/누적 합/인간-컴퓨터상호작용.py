import sys
input = sys.stdin.readline

S = list(input().rstrip())
q = int(input())

prefix = []

def prefixSum():
    global alpha
    global lt 
    global rt

    # 누적합 리스트 세팅
    if S[0] == alpha:
       prefix[0] = 1
    else :
       prefix[0] = 0
    for i in range(1,len(S)):
        prefix[i] = prefix[i-1] + checkChar(S[i])

def checkChar(s):
    if s == alpha :
        return 1
    else :
        return 0



for i in range(q):
   alpha, lt, rt = input().split()
   # 누적합 함수 실행 
   print(prefix[int(rt)-1]-prefix[int(lt)-1])
    
