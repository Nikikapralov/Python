data = input().lower()
amount_of_words = 0


def find_the_count(word, amount_of_words_new, start=0):
    while start != -1:
        start = data.find(word, start)
        if start == -1:
            break
        else:
            amount_of_words_new += 1
            start += 1
    return amount_of_words_new


amount_of_words = find_the_count('sun', amount_of_words)
amount_of_words = find_the_count('fish', amount_of_words)
amount_of_words = find_the_count('water', amount_of_words)
amount_of_words = find_the_count('sand', amount_of_words)

print(amount_of_words)