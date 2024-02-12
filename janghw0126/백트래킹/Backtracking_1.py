import sys
input=sys.stdin.readline
#자연수 N과 M을 입력받는다.
N,M=map(int,input().split())

#답을 출력할 result 리스트를 선언한다.
result=[]

#문제 해결을 위한 함수 solution을 정의한다.
def solution():
    #만약 리스트의 크기가 M이라면 모든 고른 것이 되므로 해답이 된다.
    if len(result)==M:
        #리스트의 각 요소를 문자열로 변환한 후 공백을 기준으로 곃합하여 결과를 출력한다.
        return print(' '.join(map(str,result)))
    #자릿수가 아직 안찼으면 수행할 반복문이다.
    for i in range(N):
        #만약 숫자 i+1이 result 리스트에 없는 경우에만 수행할 문이다.->중복된 숫자를 선택하지 않기 위한 조건이다.
        if i+1 not in result:
            #result리스트에 해당 숫자를 추가한다.
            result.append(i+1)
            #다음 자릿수의 숫자를 넣기 위해 재귀적으로 solution함수를 호출한다.
            solution()
            #함수 호출 후에는 해당 자릿수에서의 선택이 끝났으므로, result 리스트에서 마지막에 추가된 숫자를 제거한다.
            result.pop()
#위의 과정을 반복하여 모든 경우의 수를 찾는다.
solution()