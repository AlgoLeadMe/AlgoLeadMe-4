import sys
input = sys.stdin.readline
n = int(input()) # 도시의 개수
distance = [int(x) for x in input().split()] # 거리 리스트
city = [int(x) for x in input().split()] # 도시 주유 가격 리스트

hap = 0
oil_price = city[0]

for i in range(n-1):
    if oil_price > city[i]:
        oil_price = city[i] # 변동된 주유가격
    hap += (oil_price*distance[i])
print(hap)
