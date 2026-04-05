participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    dict = {}
    for participant_person in participant:
        if participant_person in dict:
            dict[participant_person] += 1
        else:
            dict[participant_person] = 1

    for completion_person in completion:
        dict[completion_person] -= 1
    
    for answer in dict:
        if dict[answer] != 0:
            return answer

print(solution(participant, completion))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))