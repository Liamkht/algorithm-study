seat_count = 9
vip_seat_array = [4, 7]
memo = {
    1: 1,
    2: 2
}

# 1. vip석은 무조건 자기 자신만 
# 2. 그 외 자석은 자기 자신 + 왼쪽 + 오른쪽 경우
# 3. vip석 바로 왼쪽과 오른쪽 좌석 각각은 왼쪽 : 자기 자신 + 왼쪽

# 1. 숫자를 써보면서 발견해보기
# [1, 2] --> [1, 2], [2, 1]  -> 2
# [1, 2, 3] --> [1, 2, 3], [1, 3, 2], [2, 1, 3] -> 3
# [1, 2, 3, 4] --> [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [2, 1, 3, 4], [2, 1, 4, 3] -> 5
# 피보나치 수열?
# 2. 점화식으로 써보기
# 좌석이 n개만큼 있다
# 1, 2, 3, ... n-2 n-1 n
# n번째 티켓을 가진 사람이 앉을 수 있는 방법
# 1. n번째 좌석에 앉거나
#  좌석이 n-1개만큼 있고 사람도 n-1번째 티켓까지 가진 사람이 있는 상황 
# 2. n-1번째 좌석에 앉거나
#   n-1번째 사람은 무조건 n번째 좌석에 앉아야한다
#    좌석이 n-2개만큼 있고 사람도 n-2번째 티켓까지 가진 사람이 있는 상황
# 따라서 F(n) = F(n-1) + F(n-2) ==> 피보나치 수열

def fibo_dynamic_programming(n, fibo_memo):
    if n in fibo_memo:
        return fibo_memo[n]
    
    nth_fibo = fibo_dynamic_programming(n-1, fibo_memo) + fibo_dynamic_programming(n-2, fibo_memo)
    fibo_memo[n] = nth_fibo
    
    return nth_fibo


def get_all_ways_of_theater_seat(total_count, fixed_seat_array):
    all_ways = 1
    current_index = 0
    for fixed_seat in fixed_seat_array:
        fixed_seat_index = fixed_seat - 1
        count_of_ways = fibo_dynamic_programming(fixed_seat_index - current_index, memo)
        all_ways *= count_of_ways
        current_index = fixed_seat_index + 1
    count_last_ways = fibo_dynamic_programming(total_count - current_index, memo)
    all_ways *= count_last_ways
    return all_ways


# 12가 출력되어야 합니다!
print(get_all_ways_of_theater_seat(seat_count, vip_seat_array))

print("정답 = 4 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(9,[2,4,7]))
print("정답 = 26 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(11,[2,5]))
print("정답 = 6 / 현재 풀이 값 = ", get_all_ways_of_theater_seat(10,[2,6,9]))