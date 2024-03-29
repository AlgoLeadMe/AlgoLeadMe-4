from collections import Counter

odd = 0 # 홀수 개인 알파벳 수
odd_alphabet = '' # 홀수 개인 알파벳
answer = ''

# 영어이름
name = input() 

# 각 알파벳 개수 구하고 오름차순으로 정렬
count_name = dict(sorted(Counter(name).items())) 

# 홀수개인 알파벳 수 구하기 그리고 홀수개인 알파벳 구하기
for key, value in count_name.items():
    if value%2==1:
        odd += 1
        odd_alphabet = key

# 만약 홀수개인 알파벳이 2개 이상이라면 팰린드롬을 만들 수 없음
if odd > 1:
    print("I'm Sorry Hansoo")
else:
    for key, value in count_name.items():
            answer += (key*(value//2))
    print(answer + odd_alphabet + answer[::-1])
