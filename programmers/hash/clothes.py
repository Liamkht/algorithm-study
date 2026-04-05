clothes = [["yellow_hat", "headgear"], 
        ["blue_sunglasses", "eyewear"], 
        ["green_turban", "headgear"]]
# 각 의상별 공통의상 종류 수부터 따지기
# 그리고 추가로 입는 횟수 더해주기(name의 갯수)


def solution(clothes):
    dict = {}
    for name, kind in clothes:
        if kind in dict:
            dict[kind].append(name)
        else:
            dict[kind] = [name]
    answer = 1
    for key in dict:
        answer *= (len(dict[key])+1)
    return answer - 1


    

    

print(solution(clothes))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))