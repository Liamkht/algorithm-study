import sys
N = int(sys.stdin.readline())
for _ in range(N):
    string = input()
    # 짝이 맞는 게 하나라도 있는지 없는지 비교해서
    # 안 맞는 게 하나라도 있으면 바로 NO 반환
    # 그렇지 않으면 YES (이 문제에선 개수는 상관없음)
    if ("N" in string) != ("S" in string):
        print("No")
    elif ("E" in string) != ("W" in string):
        print("No")
    else:
        print("Yes")