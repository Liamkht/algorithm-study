input = "abcba"

# 첫번째와 맨 마지막이 같아야하고 idx => 0 == len() -1
# 두번째와 맨 마지막 전이 같아야하고 idx => 1 == len() -2
# 언제까지? 음 최소와 최대가 같아질 때까지 확인

def is_palindrome(string):
    current_min = 0
    current_max = len(string)-1
    while current_min <= current_max:
        if string[current_min] != string[current_max]:
            return False
        elif string[current_min] == string[current_max]:
            current_min += 1
            current_max -= 1

    return True


print(is_palindrome(input))
print(is_palindrome("a"))