import sys

N=int(input())

energy_weight=list(map(int,input().split()))

#최댓값을 갱신하는 변수를 선언한다.
ans=0

#최댓값 갱신해주는 재귀 함수를 선언한다.
def max_energy(m):
    global ans
    # 구슬이 두 개가 남았을 경우에 최댓값을 갱신해준다.
    if len(energy_weight)==2:
        ans=max(ans,m)
        return
    # 에너지의 합을 누적해서 구해준다.
    for i in range(1,len(energy_weight)-1):
        ball=energy_weight[i-1]*energy_weight[i+1]
        v=energy_weight.pop(i)
        max_energy(m+ball)
        # 에너지의 최댓값을 갱신한 후에, 제거했던 에너지 구슬을 다시 삽입해준다.
        energy_weight.insert(i,v)

max_energy(0)
print(ans)