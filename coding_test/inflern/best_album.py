from collections import defaultdict
def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    dict = defaultdict(list)
    for i in range(len(genre_array)):
        dict[genre_array[i]].append((i, play_array[i]))
    # 장르를 재생수 합이 큰 순으로 정렬
    sorted_genre = sorted(dict, key=lambda k: sum(p for _, p in dict[k]), reverse = True)
    answer = []
    for genre in sorted_genre:
        songs = sorted(dict[genre], key=lambda x: x[1], reverse= True)
        for idx, play in songs[:2]:
            answer.append(idx)
    return answer


print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))