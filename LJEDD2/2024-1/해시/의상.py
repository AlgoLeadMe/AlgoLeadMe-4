from functools import reduce

def solution(clothes):
    # 각 종류별 가진 의상리스트를 생성 (종류:[이름, 이름, ...])
    closet = {} 
    for name, kind in clothes:
        closet[kind] = closet.get(kind, []) + [name]
    
    # A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수
    # ex ) (모자 갯수 + 1) (안경 갯수 + 1) - (모두 안 입는 1가지의 경우) 
    result = reduce(lambda x, y: x * (len(y) + 1), closet.values(), 1)
    
    return result - 1
