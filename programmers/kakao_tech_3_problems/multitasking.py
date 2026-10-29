import sys
def main():
    N, T = map(int, sys.stdin.readline().split())
    arr = list(map(int, sys.stdin.readline().split()))
    answer = [0]*N
    current_time = 0
    # 4, 2, 3  0   => 1바퀴 돌면 1, 2, 3   3   2바퀴돌면 1, 0, 3    5    => 3바퀴돌면 1, 0, 0  8
    # 만약 모두 0 이 아니면 다 0이 될때까지 돌아야함
    while any(x!=0 for x in arr):
        for i in range(N):
            if arr[i] == 0:
                continue
            else:
        
                if arr[i] < T:
                    current_time += arr[i]
                    arr[i] -= arr[i]
                    answer[i] = current_time
          

                elif arr[i] > T:
                    current_time += T
                    arr[i] -= T
                    answer[i] = current_time

                elif arr[i] == T:
                    current_time += T
                    arr[i] -= T
                    answer[i] = current_time
    print(answer)



if __name__=="__main__":
    main()