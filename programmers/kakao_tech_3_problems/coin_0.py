import sys
def main():
    N, K = map(int, sys.stdin.readline().split())
    coin_access = []
    count = 0 # 쓸 수 있는 최대크기의 동전을 쓰는 게 항상 최선이다.
    
    for i in range(N):
        A = int(sys.stdin.readline())
        coin_access.append(A)
    
    for coin in reversed(coin_access):
        if K == 0:
            break
        
        count += K // coin
        K = K % coin
    print(count)

if __name__=="__main__":
    main()