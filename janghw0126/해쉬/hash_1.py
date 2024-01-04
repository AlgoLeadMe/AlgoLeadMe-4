participant=["leo", "kiki", "eden"]
completion=["eden", "kiki"]

def solution(participant,completion):
    HashTable={}
    sumhash=0
    #파이썬에서 []->리스트, ()-> 튜플이나 함수호출
    for part in participant:
        HashTable[hash(part)]=part
        sumhash+=hash(part)

    for com in completion:
        sumhash-=hash(com)

    return HashTable[sumhash]

print(solution(participant, completion))