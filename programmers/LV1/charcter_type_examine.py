survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
def solution(survey, choices):
    answer = ""
    # survay 첫번째 캐릭터는 비동의 관련 선택지 선택하면 받는 성격 유형
    # survay 두번째 캐릭터는 동의 관련 선택지 선택하면 받는 성격 유형
    dict = {}
    for i in range(len(survey)):
        if survey[i][0] not in dict:
            dict[survey[i][0]] = 0
        if survey[i][1] not in dict:
            dict[survey[i][1]] = 0
        if choices[i] < 4:
            dict[survey[i][0]] += (4-choices[i])
        elif choices[i] > 4:
            dict[survey[i][1]] += (choices[i]-4)
        else:
            continue
    
    if 'R' and 'T' in dict:
        if dict['R'] > dict['T']:
            answer += 'R'
        elif dict['R'] < dict['T']:
            answer += 'T'
        else:
            answer += 'R'
    else:
        answer += 'R'
    if 'C' and 'F' in dict:
        if dict['C'] > dict['F']:
            answer += 'C'
        elif dict['C'] < dict['F']:
            answer += 'F'
        else:
            answer += 'C'
    else:
        answer += 'C'
    if 'J' and 'M' in dict:
        if dict['J'] > dict['M']:
            answer += 'J'
        elif dict['J'] < dict['M']:
            answer += 'M'
        else:
            answer += 'J'
    else:
        answer += 'J'
    if 'A' and 'N' in dict:
        if dict['A'] > dict['N']:
            answer += 'A'
        elif dict['A'] < dict['N']:
            answer += 'N'
        else:
            answer += 'A'
    else:
        answer += 'A' 
    return answer
print(solution(survey, choices))
print(solution(["TR", "RT", "TR"], [7, 1, 3]))