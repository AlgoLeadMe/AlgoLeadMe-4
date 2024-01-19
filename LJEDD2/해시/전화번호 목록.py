def solution(phone_book):
    phone_book.sort()
    size = len(phone_book)
    
    for i in range(1, size):
        # 다음 문자열이 앞문자열로 시작하는게 하나라도 있는지 검사 .startswith() 
        if phone_book[i].startswith(phone_book[i-1]):
            return False
    else:
        return True
    
    

# # 잘못된 접근 
# def solution(phone_book):
#     phone_book.sort()
#     size = len(phone_book)
#     for i in range(1,size):
#         # 단순히 포함되는지만 보기 때문에 접두사인지 판단 필요 
#         if phone_book[i-1] in phone_book[i]:
#             return False
#     return True
