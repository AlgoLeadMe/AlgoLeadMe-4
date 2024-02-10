S = input()

S_dic = {}
gap = 1

while S not in S_dic:
    for i in range(len(S)):
        string = S[i:i+gap]
        if i+gap > len(S):
            break
        S_dic[string] = 1
    gap+=1
    
print(len(S_dic))
