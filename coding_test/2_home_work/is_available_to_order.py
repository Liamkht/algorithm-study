shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]
#  shop_orders 반복문을 돌면서 하나씩 꺼내고
# shop_menus안에 있는지 없는지로 따져서 만약 없으면 false

def is_available_to_order(menus, orders):
    menu_set = set(menus)
    for order in orders:
        if order not in menu_set: # set을 사용해서 O(1)로 바로 확인 가능
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)