import sys

input = sys.stdin.readline

def dfs(idx, password):
  if len(password) == l:
    vowel_count = 0
    consonant_count = 0

    for letter in password:
      if letter in vowels:
        vowel_count += 1

      else:
        consonant_count += 1

    if vowel_count >= 1 and consonant_count >= 2:
      print(password)

    return

  if idx >= len(characters):
    return

  dfs(idx + 1, password + characters[idx])
  dfs(idx + 1, password)

l, c = map(int, input().rstrip('\n').split())
characters = list(input().rstrip('\n').split())

characters.sort()

vowels = ['a', 'e', 'i', 'o', 'u']
vowels = set(vowels)

dfs(0, "")
