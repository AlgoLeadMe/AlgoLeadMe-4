n = int(input())
equipList = list(map(int,input().split()))
equipList.sort()

m = int(input())
targetList = list(map(int,input().split()))

answer = [] 

for target in targetList:

    low = 0
    high = len(equipList) - 1

    while low <= high:
        middle = (high+low)//2
        if target not in equipList:
            answer.append("no")
            break 
        if target == equipList[middle]:
            answer.append("yes")
            break
        elif target < equipList[middle]:
            high = middle -1 
            
        else :
            low = middle  + 1
for x in answer:
  print(x, end = ' ')
