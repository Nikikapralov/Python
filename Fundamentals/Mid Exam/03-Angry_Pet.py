items = [int(item) for item in input().split()]
entry_point = int(input())  # That is the index of the item Tom is going to start breaking from.
array_items_left = items[0:entry_point]
array_items_right = items[entry_point + 1:]
left_sum = 0
right_sum = 0
type_of_item = input()
positive_negative_all = input()

items_left = []
items_right = []


if type_of_item == 'cheap':
    for item_left in array_items_left:
        if item_left < items[entry_point]:
            items_left.append(item_left)
    for item_right in array_items_right:
        if item_right < items[entry_point]:
            items_right.append(item_right)

elif type_of_item == 'expensive':
    for item_left in array_items_left:
        if item_left >= items[entry_point]:
            items_left.append(item_left)
    for item_right in array_items_right:
        if item_right >= items[entry_point]:
            items_right.append(item_right)

if positive_negative_all == 'positive':
    for item in items_left:
        if item > 0:
            left_sum += item
    for item_2 in items_right:
        if item_2 > 0:
            right_sum += item_2
elif positive_negative_all == 'negative':
    for item in items_left:
        if item < 0:
            left_sum += item
    for item_2 in items_right:
        if item_2 < 0:
            right_sum += item_2
elif positive_negative_all == 'all':
    left_sum = sum(items_left)
    right_sum = sum(items_left)

if left_sum >= right_sum:
    print(f'Left - {left_sum}')
else:
    print(f'Right - {right_sum}')






