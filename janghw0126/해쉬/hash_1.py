def solution(participant, completion):
    #파이썬에서 dict 자료형이 해쉬 맵 역할을 수행하므로 별도의 라이브러리를 임포트하지 않아도 됌.
    #hashDict와 sumHash를 초기화한다.
    hashDict = {} 
    sumHash = 0
    
    for part in participant:
        # 1. Participant의 dictionary를 만든다.
        hashDict[hash(part)] = part
        # 2. Participant의 sum(hash)를 구한다.
        sumHash += hash(part)
    
    # 3. completion의 sum(hash)를 뺀다.
    for comp in completion:
        sumHash -= hash(comp)
    
    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다.

    return hashDict[sumHash]