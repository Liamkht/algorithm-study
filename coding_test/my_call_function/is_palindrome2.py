input = "abcba"


def is_palindrome(string):
    if len(string) <= 1: # 문자열의 길이가 1보다 작거나 같을 때 ==> 무조건 회문
        return True
    elif string[0] != string[-1]: # 문자열의 첫번째와 맨 마지막이 다르다면 ==> 회문 x
        return False
    return is_palindrome(string[1:-1]) # ==> 문자열 계속 축소시키기


print(is_palindrome(input))