sentence=" The first character is a blank"

#문장을 공백을 기준으로 나누고 빈 문자열을 제외한다.
word=[word for word in sentence.split(" ") if word]

print(len(word)) 