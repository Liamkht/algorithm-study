clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
def solution(clothes):
    dict = {}
    # 일단은 개별 의상 하나씩 가지는 경우 즉 갯수
    # 의상의 종류별 개수를 세서 각각의 의상의 종류별 개수에
    # +1(안 입는 경우)을 해서 다 곱한 후 거기서 -1(아무것도 안 입는 경우)만 제외해주면 됨
    
    for cloth in clothes:
        name, category = cloth[0], cloth[1]
        if category in dict:
            dict[category].append(name)
        else:
            dict[category] = [name]
    # 여기서 각 종류에 +1을 한 후 곱하고 -1을 하면 최종 갯수
    # 여기서 키를 다 돌면서 value의 갯수+1을하고 곱하면
    answer = 1
    for key in dict:
        answer *= (len(dict[key]) + 1)
    answer -= 1

    return answer
print(solution(clothes))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))