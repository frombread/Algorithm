import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())
products = deque(list(map(int, input().split())))

power_bar = []
cnt = 0

while products:
    if products[0] in power_bar: # 앞에서 한개씩 빼서 콘센트에 있으면 그냥 빼버린다
        products.popleft()
        continue

    if len(power_bar) < N:
        power_bar.append(products.popleft())
        continue

    change_product, product_index = 0, 0 # 바꿔줄꺼 초기화
    for mounted_product in power_bar: # 콘센트에 꼽혀있는 물건들 중에
        if not mounted_product in products: # 물건들이 리스트에 없으면
            change_product = mounted_product # 바꿔주는거고
            break

        elif products.index(mounted_product) > product_index: # 있으면 인덱스 확인해서
            product_index = products.index(mounted_product) # 인덱스 바꿔주고
            change_product = mounted_product # 바꾸기

    power_bar[power_bar.index(change_product)] = products.popleft() # 바꿔주는거
    cnt+=1

print(cnt)