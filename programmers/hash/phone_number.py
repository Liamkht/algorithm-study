phone_book = ["119", "97674223", "1195524421"]
# phone_book을 먼저 정렬 후 바로 다음에 놓이는 인접한 애랑만 비교해 나가다가
# 만약 그 쌍이 하나도 없으면 접두어가 없는 거니까 true 하나라도 있으면 false
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i+1].startswith(phone_book[i]):
            return False

    return True
print(solution(phone_book))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))