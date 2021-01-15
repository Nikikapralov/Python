class DictionaryWithSynonyms:
    def __init__(self, n):
        self.n = int(n)
        self.synonym_dict = {}
        self.word_synonym_input(self.n)

    def word_synonym_input(self, n):
        for _ in range(n):
            word_key = input()
            synonym_value = input()
            if word_key in self.synonym_dict:
                self.synonym_dict[word_key].append(synonym_value)
            else:
                self.synonym_dict[word_key] = [synonym_value]
        print(self.print_synonyms(self.synonym_dict))

    def print_synonyms(self, dictionary_of_synonyms):
        result = ''
        for word_key, synonym_value in dictionary_of_synonyms.items():
            result += f'{word_key} - {", ".join(synonym_value)}\n'
        return result


dictionary_1 = DictionaryWithSynonyms(input())
