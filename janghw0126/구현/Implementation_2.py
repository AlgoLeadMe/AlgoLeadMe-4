#1. 알파벳 대소문자로 이루어진 단어를 입력받는다.
#2. 단어의 문자들을 전부 알파벳 대문자로 변경한다.
word=input().upper()

#3. set() 을 이용해 중복된 문자들을 제거해주고 남은 고유한 문자들을 정렬해주는 list를 선언한다.
word_list=list(set(word))

#4. 알파벳의 갯수를 저장하기 위한 list cnt를 선언한다.
cnt=[]

#5. 반복문을 통해서 중복된 문자의 갯수를 세고 cnt에 추가한다.
for char in word_list:
    count=word.count(char)
    cnt.append(count)

#6. 만약 가장 많이 사용된 알파벳이 2개 이상이라면 "?"을 출력한다.
if cnt.count(max(cnt))>=2:
    print("?")
#7. 아니라면 가장 많이 사용된 문자의 인덱스를 알아내어 중복된 문자들이 제거된 배열인 word_list의 인덱스에 있는 문자를 알아내면 된다.
else:
    print(word_list[(cnt.index(max(cnt)))].upper())




