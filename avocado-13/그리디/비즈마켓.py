n, m = map(int,input().split())

a_list = sorted(list(map(int,input().split())), reverse = True) # 내림차순으로 정렬
b_list = sorted(list(map(int,input().split()))) # 오름차순으로 정렬

ans = 0 

for a,b in zip(a_list,b_list): # zip은 두 리스트의 길이가 다를 때 짧은 것에 맞추므로 리스트 슬라이싱 등의 길이 맞춤은 굳이 하지 않았다. 
    if (a - b < 0):
        continue
    ans += (a - b)

print(ans)



# 다른 사람의 코드
# import sys
# input=sys.stdin.readline

# def func():
#     n,m=map(int,input().split())
#     product=list(map(int,input().split()))
#     payment=list(map(int,input().split()))
#     product.sort(reverse=True)
#     payment.sort()
#     answer=0

#     for i in range(min(n,m)):
#         if product[i]-payment[i]<0:
#             return answer
#         answer+=product[i]-payment[i]
#     return answer

# print(func())