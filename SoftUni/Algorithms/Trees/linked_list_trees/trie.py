"""
Trie is a special linked list type of tree that is used for storing characters and a fast lookup
of words.

How does a Trie work?

A Trie has a node that has a dictionary as a class variable.
Inside this dictionary we store all the branches as keys being the character and the node itself
being the value, which holds another dictionary.
Each node is marked as being terminal or not. If a not is terminal, that is the signal that we
have reached the end of our word string.

Tries are used for word prediction and search suggestions. Lookup in the trie dictionary is always
O(N) where length is the length of the word we are searching for in the dictionary.
Trie is useful where we want to predict all words that have a certain common root.
"""


class TrieNode:
    def __init__(self):
        self.terminal: bool = False


class Trie:

    def insert(self, string: str):
        """
        Insert a string into the Trie.
        @param string: String to be inserted.
        @return: Self for chaining.
        """
        return self

    def delete(self, string: str):
        """
        Delete a string from the Trie.
        @param string: String to be deleted.
        @return: Self for chaining.
        """
        return self

    def search(self, string: str) -> bool:
        """
        Search for a string in the Trie. If inside the Trie, return True, else False.
        @param string: String to search for in the Trie.
        @return: True/False
        """
        return False

    def word_prediction(self, word_root: str) -> list[str]:
        """
        According to the provided root of the word, return a list with all
        possible words that can be formed from the symbols inserted in to the Trie.
        @param word_root: The rood of the word. amaz will return amazon,
        amazing, amazed if those 3 are contained in the Trie.
        @return: A list holding all strings that can be formed
        from the chosen root that are inside the Trie.
        """
        pass
