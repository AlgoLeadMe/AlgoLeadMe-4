import sys

input = sys.stdin.readline

n, m = map(int, input().split())

word_list = [x for _ in range(n) if len(x := input().rstrip()) >= m]

dic = {}
for word in word_list:
    dic[word] = dic.get(word, 0) + 1

sorted_words = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, count in sorted_words:
    print(word)

