import sys
def main():
    N = int(sys.stdin.readline())
    current_time = 0
    total_time = 0
    p_list = list(map(int, sys.stdin.readline().split()))
    p_list.sort()
    for i in range(N):
        current_time += p_list[i]
        total_time += current_time
    print(total_time)



if __name__=="__main__":
    main()