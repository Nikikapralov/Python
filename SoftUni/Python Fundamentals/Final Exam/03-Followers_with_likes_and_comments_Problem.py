followers_dict = {}
while True:
    command = input().split(': ')
    if command[0] == 'Log out':
        break
    elif command[0] == 'New follower':
        username = command[1]
        if username in followers_dict:
            continue
        elif username not in followers_dict:
            followers_dict[username] = [0, 0]
    elif command[0] == 'Like':
        username = command[1]
        likes_count = int(command[2])
        if username not in followers_dict:
            followers_dict[username] = [likes_count, 0]
        elif username in followers_dict:
            old_likes = int(followers_dict[username][0])
            new_likes = old_likes + likes_count
            followers_dict[username][0] = new_likes
    elif command[0] == 'Comment':
        username = command[1]
        if username not in followers_dict:
            followers_dict[username] = [0, 1]
        elif username in followers_dict:
            followers_dict[username][1] += 1
    elif command[0] == 'Blocked':
        username = command[1]
        if username not in followers_dict:
            print(f"{username} doesn't exist.")
        elif username in followers_dict:
            followers_dict.pop(username)
print(f'{len(followers_dict)} followers')
for key, value in sorted(followers_dict.items(), key=lambda x: (-(x[1][0] + x[1][1]), x[0])):
    print(f'{key}: {sum(value)}')
