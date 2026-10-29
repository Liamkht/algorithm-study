# 완주하지 못한 선수는 무조건 단 한 명
# 참가자 이름은 알파벳 소문자 , 참가자 중에는 동명이인 가능

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
def solution(participant, completion):
    dict = {}

    #1. 완주자 명단을 이름별 개수로 세어본다.
    for name in completion:
        dict[name] = dict.get(name, 0) + 1

    #2 참가자를 순서대로 돌면서 완주자 개수를 하나씩 깎는다.
    for name in participant:
        if dict.get(name, 0) == 0:
            return name
        dict[name] -= 1

print(solution(participant, completion))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))