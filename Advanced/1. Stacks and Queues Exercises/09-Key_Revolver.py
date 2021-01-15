from collections import deque
price_of_bullet = int(input())
gun_barrel_size = int(input())
bullets = [int(bullet) for bullet in input().split()]
bullets = deque(bullets[::-1])
total_bullets = len(bullets)
stack_locks = [int(lock) for lock in input().split()]
stack_locks = stack_locks[::-1]
value_of_intelligence = int(input())
ammo_shot = 0
while True:
    if not stack_locks:
        print(f'{len(bullets)} bullets left. Earned ${value_of_intelligence - ((total_bullets - len(bullets)) * price_of_bullet)}')
        break
    elif not bullets:
        print(f"Couldn't get through. Locks left: {len(stack_locks)}")
        break
    current_bullet = bullets.popleft()
    current_lock = stack_locks.pop()
    if current_bullet <= current_lock:
        print('Bang!')
    else:
        stack_locks.append(current_lock)
        print('Ping!')
    ammo_shot += 1
    if ammo_shot == gun_barrel_size:
        ammo_shot = 0
        if bullets:
            print('Reloading!')
        else:
            continue


