import string
import wordset.wordset as ws


class LetterNode:

    def __init__(self, letter):
        self.letter = letter
        self.prev = set()
        self.next = set()

    def add_prev(self, letter):
        self.prev.add(letter)

    def add_next(self, letter):
        self.next.add(letter)

    def random_next_letter(self, letter):
        if letter in self.next:
            return self.next[letter]
        else:
            raise Exception('Letter not found in the dictionary.')


def _set_dict():
    all_letters = dict()

    for letter in list(string.ascii_lowercase):
        all_letters[letter] = LetterNode(letter)

    return all_letters


class Trie:

    def __init__(self, word_set):
        self.word_one = _set_dict()
        self.word_two = _set_dict()
        self.word_three = _set_dict()
        self.word_four = _set_dict()
        self.word_five = _set_dict()
        self.order = [self.word_one, self.word_two, self.word_three, self.word_four, self.word_five]

        for word in word_set:
            for i, dictionary in enumerate(self.order):
                if i == 0:
                    dictionary[word[i]].add_next(self.word_two[word[i + 1]])
                elif i == 4:
                    dictionary[word[i]].add_prev(self.word_four[word[i - 1]])
                else:
                    dictionary[word[i]].add_next(self.order[i + 1][word[i + 1]])
                    dictionary[word[i]].add_prev(self.order[i - 1][word[i - 1]])

    def remove_letter_all(self, letter):
        for dictionary in self.order:
            del dictionary[letter]
            for key in dictionary.keys():
                dictionary[key].next.remove(letter)
                dictionary[key].prev.remove(letter)

    def remove_letter_single(self, letter, position):
        del self.order[position][letter]
        if position != 4:
            for next_keys in self.order[position + 1].keys():
                self.order[position + 1][next_keys].prev.remove(letter)
        if position != 0:
            for prev_keys in self.order[position - 1].keys():
                self.order[position + 1][prev_keys].next.remove(letter)

    def only_letter(self, letter, position):
        for node_key in self.order[position].keys():
            if letter != node_key:
                del self.order[position][node_key]

    def clean_trie(self):
        for i, dictionary in enumerate(self.order):
            pass


if __name__ == '__main__':
    words = ws.WordSet()

    trie = Trie(words.get_solutions())

    print(trie.word_one)
