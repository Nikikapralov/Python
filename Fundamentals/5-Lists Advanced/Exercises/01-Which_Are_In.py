unique_list = input().split(', ')
list_1 = input().split(', ')
unique_list_copy = unique_list.copy()
check = [unique_item for unique_item in unique_list for item in list_1 if unique_item in item]
check_final = []
test = [check_final.append(x) for x in check if x not in check_final]
print(check_final)