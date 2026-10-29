import sys
N = int(input())
cat_score = 0
queen_score = 0
winner = []
is_draw = True
reach_100 = False
for i in range(N):
    if cat_score >= 100 or queen_score >= 100:
        reach_100 = True
        if cat_score > queen_score:
            print("C")
            print(cat_score, queen_score)
        elif cat_score < queen_score:
            print("H")
            print(cat_score, queen_score)
        break
    card1, card2 = map(int, sys.stdin.readline().split())
    if card1 > card2:
        cat_score += card1
        winner.append("C")
    elif card1 < card2:
        queen_score += card2
        winner.append("H")
    else:
        cat_score += 0
        queen_score += 0
        winner.append("D")
if reach_100 == False:
    if cat_score > queen_score:
        print("C")
        print(cat_score, queen_score)
    elif cat_score < queen_score:
        print("H")
        print(cat_score, queen_score)
    else:
        for k in range(len(winner)-1, -1, -1):
            if winner[k] == "C":
                is_draw = False
                print("C")
                print(cat_score, queen_score)
                break
            elif winner[k] == "H":
                print("H")
                print(cat_score, queen_score)
                is_draw = False
                break
            else:
                continue
        if is_draw == True:
            print("D")
            print(cat_score, queen_score)




    







    



