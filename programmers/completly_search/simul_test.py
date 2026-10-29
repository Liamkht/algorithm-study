answers = [1,2,3,4,5]
def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [0, 0, 0]
    # 각각 학생별로 정답의 크기만큼 규칙을 만들어서 찍기 배열을 만들어놓고
    # answers와 돌리면서 맞으면 count 증가시키는 방식으로 그리고 count 배열에다 담고
    # 순서에 따라 1, 2, 3 반환하도록 ?
    for i in range(len(answers)): # i = 0, 1, 2, 3, 4
        if answers[i] == pattern1[i%len(pattern1)]:
            scores[0] += 1
        if answers[i] == pattern2[i%len(pattern2)]:
            scores[1] += 1
        if answers[i] == pattern3[i%len(pattern3)]:
            scores[2] += 1
    answer = []
    max_score = max(scores)
    for i in range(3):
        if scores[i] == max_score:
            answer.append(i + 1)
    return answer
print(solution(answers))
print(solution([1,3,2,4,2]))