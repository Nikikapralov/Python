import sys
usernames_to_submissions_points = {}
submissions = {}
max_points_dict = {}
while True:
    is_language_in_list = False
    command = input()
    if command == 'exam finished':
        break
    command_split = command.split('-')
    if len(command_split) == 3:
        username = command_split[0]
        language = command_split[1]
        points = command_split[2]
        int_points = int(points)
        if username not in usernames_to_submissions_points:
            usernames_to_submissions_points[username] = [[language, int_points]]
        elif username in usernames_to_submissions_points:
            for list_ in usernames_to_submissions_points[username]:
                if language in list_:
                    if list_[1] < int_points:
                        list_[1] = int_points
                        is_language_in_list = True
                        break
                elif language not in list_:
                    continue
            if not is_language_in_list:
                usernames_to_submissions_points[username].append([language, int_points])
        if language in submissions:
            submissions[language] += 1
        elif language not in submissions:
            submissions[language] = 1
    elif len(command_split) == 2:
        banned_name = command_split[0]
        if banned_name in usernames_to_submissions_points:
            usernames_to_submissions_points.pop(banned_name)

print('Results:')
for key, nested_list in usernames_to_submissions_points.items():
    max_points = -sys.maxsize
    for value_list in nested_list:
        for value in value_list:
            if isinstance(value, int):
                if value > max_points:
                    max_points = value
                    max_points_dict[key] = value
            else:
                continue
for name, points in sorted(max_points_dict.items(), key=lambda x: (-x[1], x[0])):
    print(f'{name} | {points}')
print(f'Submissions:')
for language_1, submission_count in sorted(submissions.items(), key=lambda x: (-x[1], x[0])):
    print(f'{language_1} - {submission_count}')
print(max_points_dict)
print(usernames_to_submissions_points)
print(submissions)

