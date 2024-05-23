"""
https://www.iflscience.com/scientists-have-discovered-a-new-way-to-count-and-its-actually-really-important-74327

CVM is a new counting method that uses statistics to approximate the count of distinct elements in a collection.
Compared to a normal count, CVM is more memory efficient.

Algorithm:
Define max set size: 100
Fill the set with 100 elements.
If the set is full, throw a coin for each element. If 0, keep it. Otherwise, delete it to make space.
Continue filling the set, except if we encounter a word already in the set, throw a coin to see if we keep or delete it.
Throw the coin N amount of times (N being the number of iterations).
At the end, multiply the unique words in the set by 2 ** N amount of iterations it took us to loop through the collection.

PRO:
- Memory efficient. Useful if you cannot fill all distinct words into memory.

- Increasing the memory capacity of the set results in a higher precision of the answer.

CON:
- Slower than a normal count. (Multithreading can be utilized to
speed up the set refactoring after the size limit is reached,
which makes me think I should have written this in C++ to show it...)

- A bit harder to implement than a normal set passthrough.

- Returns an approximation of number of unique words, not the 100% exact count.

Application:

To be used when one requires only an approximation of the amount of unique tokens in the collection
if the those tokens are expected to be highly diverse and would overflow the memory. (If you can't do it with a simple
set passthrough, use cvm).

"""
from random import random, getrandbits
import re


with open("hamlet.txt") as file:

    hamlet_text: str = file.read()

    # Remove punctuation using regular expressions
    hamlet_text_cleaned: str = re.sub(r'[^\w\s]', '', hamlet_text)

    # Split the text into words and store them in a list
    hamlet_words: list[str] = [word.lower() for word in hamlet_text_cleaned.split()]


def cvm_count1(data, set_size=100):
    unique_words = set()
    p = 1

    for word in data:
        if word in unique_words:
            unique_words.remove(word)

        if random() < p:
            unique_words.add(word)

        if len(unique_words) >= set_size:
            new_set = unique_words.copy()
            for word in new_set:
                if bool(getrandbits(1)):
                    unique_words.remove(word)

            p /= 2

    return len(unique_words) / p

def cvm_count2(data, set_size=100):
    buffer = set()
    p = 1.0
    element_u_map = {}

    for word in data:
        if word in buffer:
            buffer.remove(word)
            del element_u_map[word]

        u = random()

        if u <= p:
            buffer.add(word)
            element_u_map[word] = u

        if len(buffer) > set_size:
            max_element = max(element_u_map, key=element_u_map.get)
            buffer.remove(max_element)
            p = element_u_map[max_element]
            del element_u_map[max_element]

    return len(buffer) / p


print("Unique words in Hamlet passthrough: ", len(set(hamlet_words)))
print("CVM:", cvm_count1(data=hamlet_words), "Set size: 100")
print("CVM:", cvm_count1(data=hamlet_words, set_size=1000), "Set size: 1000")
print("CVM:", cvm_count1(data=hamlet_words, set_size=2000), "Set size: 2000")

print("CVM2:", cvm_count2(data=hamlet_words), "Set size: 100")
print("CVM2:", cvm_count2(data=hamlet_words, set_size=1000), "Set size: 1000")
print("CVM2:", cvm_count2(data=hamlet_words, set_size=2000), "Set size: 2000")