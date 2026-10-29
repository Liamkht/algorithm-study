import sys
N = int(sys.stdin.readline())
cat_score = 0
queen_score = 0
is_reach_100 = False
is_draw = False
winner = []
for i in range(N):
    card1, card2 = map(int, sys.stdin.readline().split())
    if card1 > card2: # 쳬셔고양이 > 하트 여왕
        cat_score += card1
        winner.append("C")
    
    elif card2 > card1: # 체셔고양이 < 하트 여왕
        queen_score += card2
        winner.append("H")
    
    else: # 체셔고양이 = 하트여왕
        cat_score += 0
        queen_score += 0
        winner.append("D")

    if cat_score >= 100 or queen_score >= 100: # 둘 중 한쪽이 100점 이상의 점수에 도달하면 종료
        is_reach_100 = True
        if cat_score > queen_score:
            print("C")
        elif cat_score < queen_score:
            print("H")
        else:
            print("D")
        print(cat_score, queen_score)
        break
    

if is_reach_100 == False: # 둘 중 한쪽이 100점 이상의 점수에 도달하지 않은 경우(즉 반복문을 끝까지 돈 경우)
    if cat_score > queen_score:
        print("C")
    elif cat_score < queen_score:
        print("H")
    else: 
        for k in range(len(winner)-1, -1, -1):
            if winner[k] == "C":
                print("C")
                is_draw = False
                break
            elif winner[k] == "H":
                print("H")
                is_draw = False
                break
            elif winner[k] == "D":
                is_draw = True
                continue
        if is_draw == True:
            print("D")
    print(cat_score, queen_score)
                
