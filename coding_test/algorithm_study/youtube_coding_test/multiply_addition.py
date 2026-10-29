# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 'x' 혹은 '+'연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램
# 단 +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은
# 왼쪽에서부터 순서대로 이루어짐
def solution(s):
    num = int(s[0])
    for i in range(1, len(s)):
        int_num = int(s[i])
        if num <= 1 or int_num <= 1:
            num += int_num
        else:
            num *= int_num

        
    return num

print(solution('02984'))
print(solution('567'))