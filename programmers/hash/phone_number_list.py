phone_book = ["119", "97674223", "1195524421"]
"""
def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True
"""
def solution(phone_book):
    phone_set = set(phone_book)

    for phone in phone_book:
        prefix=""
        for num in phone:
            prefix+=num

            if prefix in phone_set and prefix != phone:
                return False
            
    return True
print(solution(phone_book))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))