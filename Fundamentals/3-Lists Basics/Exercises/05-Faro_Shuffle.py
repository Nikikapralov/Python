deck = input().split()
number_of_shuffles = int(input())
half_deck = len(deck) // 2
new_list = []
half_deck_list1 = deck[:half_deck:]
half_deck_list2 = deck[half_deck::]
for shuffle in range(number_of_shuffles):
    new_list = []
    index1 = 0
    index2 = 0
    for x in range(1, len(deck) + 1):
        if x % 2 != 0:
            new_list.append(half_deck_list1[index1])
            index1 += 1
        elif x % 2 == 0:
            new_list.append(half_deck_list2[index2])
            index2 += 1
    half_deck_list1 = new_list[:half_deck:]
    half_deck_list2 = new_list[half_deck::]
print(new_list)
