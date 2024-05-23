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

How will we search for the words amazon, amazing, amazing grace, ball?

First we need to insert each word into the Trie. Let us start with amazon and ball.
We start with the first node.


Traversal of a Tree without links to a previous node can be done by using a stack!
Otherwise known as recursion!
"""

class TrieNode:
    def __init__(self, previous_node=None):
        self.terminal: bool = False
        self.characters: dict[str, TrieNode] = {}
        self.previous_node: TrieNode | None = previous_node  # If we use a stack,
        # we don't need previous node to backtrack.


class Trie:
    def __init__(self, trie_node_class: [TrieNode] = TrieNode):
        self._first_node: TrieNode = trie_node_class()  # First node has has access to all possible chars.
        self._trie_node_class: [TrieNode] = TrieNode

    def insert(self, string: str):
        """
        Insert a string into the Trie.
        Insert each character inside the Trie.
        At the end of the string, last character, create a new blank node.
        @param string: String to be inserted.
        @return: Self for chaining.
        """
        current_node: TrieNode = self._first_node
        for character in string:
            if character not in current_node.characters.keys():
                current_node.characters[character]: TrieNode = self._trie_node_class(previous_node=current_node)

            current_node: TrieNode = current_node.characters[character]

        current_node.terminal = True

        return self

    def delete(self, string: str):
        """
        Delete a string from the Trie.
        Alternatively, we can use a stack data structure to reach the bottom and then
        start emptying the stack LIFO.
        @param string: String to be deleted.
        @return: Self for chaining.
        """
        if not string:
            return self
        # Find the bottom of the word.
        current_node: TrieNode = self._first_node
        for character in string:
            if character not in current_node.characters.keys():
                return self
            current_node: TrieNode = current_node.characters[character]

        if not current_node.terminal:
            return self

        # Start working upwards deleting links
        for index in range(len(string) - 1, -1, -1):

            character: str = string[index]
            leaf_node: TrieNode | None = current_node.previous_node

            # If node is marked as terminal, remove it, deleting the word marker. Next to remove the chars.
            if current_node.terminal:
                current_node.terminal = False

            # If a node has dependencies, break the cycle, we cannot remove the chars.
            if leaf_node.characters:
                break

            # Break coupling if node is empty
            current_node.previous_node = None
            del leaf_node.characters[character]

        return self

    def search(self, string: str) -> bool:
        """
        Search for a string in the Trie. If inside the Trie, return True, else False.
        Loop through the word until we either find no match or we find the terminal node.
        @param string: String to search for in the Trie.
        @return: True/False
        """
        current_node: TrieNode = self._first_node
        for character in string:
            if character not in current_node.characters.keys():
                return False
            current_node: TrieNode = current_node.characters[character]

        if not current_node.terminal:
            return False

        return True

    def word_prediction(self, word_root: str) -> list[str]:
        """
        According to the provided root of the word, return a list with all
        possible words that can be formed from the symbols inserted in to the Trie.
        @param word_root: The rood of the word. amaz will return amazon,
        amazing, amazed if those 3 are contained in the Trie.
        @return: A list holding all strings that can be formed
        from the chosen root that are inside the Trie.


        I just want to say I came up with this algorithm myself and I am very proud of the work I did.
        It seems to work very well and I am very happy. I didn't sleep tonight but it was totally worth it
        since now I can do word predictions! I am very, very happy. At first I tried pre-order but didnt notice a
        case with amaz and amazing (substring part of string) then tried with queue but ultimately fixed it
        all by myself (had to remove a return statement) and used pre-order traversal anyway! I feel amazing!
        """
        results: list[str] = []
        if not word_root:
            return results
        
        # Find the bottom of the word.
        current_node: TrieNode = self._first_node
        for character in word_root:
            if character not in current_node.characters.keys():
                return results
            current_node: TrieNode = current_node.characters[character]

        branches: list[str] = self._find_word_from_word_root(node=current_node)
        words: list[str] = [word_root + branch for branch in branches]
        return words

    def _find_word_from_word_root(self, node: TrieNode,
                                  word_branch: str = "",
                                  total_branches: list[str] = None) -> list[str]:
        """
        Preorder traversal will work just fine.
        Once we reach the end of the word root, we start to go towards each of the branches.
        Once we go over the whole tree, we return the word.
        @param node: Node with symbols.
        @param word_branch: The branch of the word after the root.
        @param total_branches: A place to collect all branches.
        @return:
        """
        # Place to collect all word branches.
        if total_branches is None:
            total_branches: list[str] = []

        # If no more characters and we have a word.
        if not node.characters:
            if word_branch:
                total_branches.append(word_branch)
            return total_branches

        # If more characters but terminal, and we have a word,
        # we append word but continue building next word. (No return)
        if node.terminal:
            if word_branch:
                total_branches.append(word_branch)

        # Pre-order branch out
        for char, char_node in node.characters.items():
            total_branches: list[str] = self._find_word_from_word_root(node=char_node,
                                                                       word_branch=word_branch + char,  # Build word
                                                                       total_branches=total_branches)
        return total_branches





t = Trie()
t.insert("amazon").insert("amaz").insert("amazing").insert("amazonaurous")
print(t.word_prediction(word_root="amazon"))