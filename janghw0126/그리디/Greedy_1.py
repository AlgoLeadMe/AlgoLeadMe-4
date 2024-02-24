n = str(input())
m = n.split('-')

answer = 0
# 첫번째는 -로 시작할 경우의 수가 있어서 따로 작업을 한다.
x = sum(map(int, (m[0].split('+'))))
if n[0] == '-':
    answer -= x
else:
    answer += x
# 첫번째 작업은 이미 했기때문에 인덱스 1부터 시작한다.
for x in m[1:]:
    x = sum(map(int, (x.split('+'))))
    answer -= x
print(answer)