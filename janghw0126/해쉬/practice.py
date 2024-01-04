#완주하지 못한 선수
#해쉬를 이용한 풀이 방법
#1. 참가자와 완주한 선수들 나열하는 배열 선언한다.
#2. 참가자들의 해시값을 더한 sumHash값을 구한다.
#3. 완주자들의 해시값을 sumHash에서 뺀다.
#4. 남은 해시값이 완주하지 못한 선수의 해시값이 된다.

participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

def solution(participant,completion):
    HashDict={}
    sumHash=0

    for part in participant:
        HashDict[hash(part)]=part
        sumHash+=hash(part)

    for com in completion:
        sumHash-=hash(com)
    
    return HashDict[sumHash]

print(solution(participant,completion))