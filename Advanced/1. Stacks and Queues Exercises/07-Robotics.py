from collections import deque
import time
queue_of_robots = deque()
robots = input().split(';')
dict_of_robots = {}
queue_of_products = deque()
robots_to_pop = []
for robot in robots:
    name, time_needed = robot.split('-')
    current_robot = [name, int(time_needed)]
    queue_of_robots.append(current_robot)
hours, minutes, seconds = input().split(':')
starting_time = int(seconds) + int(minutes) * 60 + int(hours) * 3600


def there_is_free_robot(current_product):
    robot_working = queue_of_robots.popleft()
    dict_of_robots[robot_working[0]] = [robot_working[1], robot_working[1]]
    current_time = time.strftime('%H:%M:%S', time.gmtime(starting_time))
    print(f'{robot_working[0]} - {current_product} [{current_time}]')


def no_free_robot(current_product):
    queue_of_products.append(current_product)


def robot_is_working():
    for key in dict_of_robots:
        dict_of_robots[key][0] -= 1
        if dict_of_robots[key][0] <= 0:
            queue_of_robots.append([key, dict_of_robots[key][1]])
            robots_to_pop.append(key)
    for item in robots_to_pop:
        dict_of_robots.pop(item)
    robots_to_pop.clear()


while True:
    product = input()
    if product == 'End':
        break
    queue_of_products.append(product)


while queue_of_products:
    starting_time += 1
    current_product = queue_of_products.popleft()
    if queue_of_robots:
        there_is_free_robot(current_product)
        if dict_of_robots:
            robot_is_working()

    elif not queue_of_robots:
        no_free_robot(current_product)
        if dict_of_robots:
            robot_is_working()



