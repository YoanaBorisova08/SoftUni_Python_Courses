from collections import deque

bullet_price = int(input())

gun_barrel_size = int(input())
current_gun_load = gun_barrel_size

bullets = list(map(int, input().split()))
locks = deque(map(int, input().split()))

pay = int(input())

while locks and bullets:
    if bullets.pop() <= locks[0]:
        locks.popleft()
        print("Bang!")
    else:
        print("Ping!")

    current_gun_load -= 1
    pay -= bullet_price

    if current_gun_load==0 and bullets:
        current_gun_load = gun_barrel_size
        print("Reloading!")


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${pay}" )