import sys
def main():
    N, M = map(int, sys.stdin.readline().split())
    bucket = [0]*N
    for i in range(N):
        bucket[i] = i+1
    print(bucket)
    for i in range(M):
        bucket_change1, bucket_change2 = map(int, sys.stdin.readline().split())
        bucket[bucket_change1-1], bucket[bucket_change2-1] = bucket[bucket_change2-1], bucket[bucket_change1-1]
    print(*bucket)



if __name__=="__main__":
    main()