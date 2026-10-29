shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]
# 가격을 내림차순으로 정렬하고 쿠폰도 내림차순으로 정렬 후
# 각각에 할인율에 맵핑하면 
# 150만원 3만원 2천원 40%, 20% ==> 90만원 + 2만 4천원 + 2천원 



def get_max_discounted_price(prices, coupons):
    prices.sort(reverse = True)
    coupons.sort(reverse = True)
    discount_prices = []
    length_short = min(len(prices), len(coupons))
    for i in range(length_short):
        prices[i] = (prices[i] - int(prices[i] * (coupons[i]*0.01)))
    
    return sum(prices)


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))