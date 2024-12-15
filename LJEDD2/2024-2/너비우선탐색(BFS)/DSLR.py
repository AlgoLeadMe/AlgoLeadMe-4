# BOJ 9019
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int,input().split())

    visited = [False] * (10001)
    queue = deque([(A,'')])
    visited[A] = True

# 수식 참고 https://velog.io/@hamsangjin/%EB%B0%B1%EC%A4%80-9019%EB%B2%88-DSLR-%ED%8C%8C%EC%9D%B4%EC%8D%AC
    while queue:
        num, order = queue.popleft()

        if num == B:
            print(order)
            break
            
        # D: D 는 n을 두 배로 바꾼다.
        # 결과 값이 9999 보다 큰 경우에는 10000 으로 나눈 나머지를 취한다.
        # 그 결과 값(2n mod 10000)을 레지스터에 저장
        D = num * 2 % 10000
        if not visited[D]:
            visited[D] = True
            queue.append((D, order + 'D'))

        # S: S 는 n에서 1 을 뺀 결과 n-1을 레지스터에 저장한다.
        # n이 0 이라면 9999 가 대신 레지스터에 저장
        S = (num - 1) % 10000
        if not visited[S]:
            visited[S] = True
            queue.append((S, order + 'S'))

        # L: L 은 n의 각 자릿수를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.
        # 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d2, d3, d4, d1이 된다
        # 첫번째 자리를 끝으로 보내버리도록 
        L = num // 1000 + (num % 1000)*10
        if not visited[L]:
            visited[L] = True
            queue.append((L, order + 'L'))

        # R: R 은 n의 각 자릿수를 오른편으로 회전시켜 그 결과를 레지스터에 저장한다.
        # 이 연산이 끝나면 레지스터에 저장된 네 자릿수는 왼편부터 d4, d1, d2, d3이 된다.
        #  마지막 숫자 데려오기
        R = num // 10 + (num % 10) * 1000
        if not visited[R]:
            visited[R] = True
            queue.append((R, order  + 'R'))