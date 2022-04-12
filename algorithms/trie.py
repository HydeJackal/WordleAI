import string


class LetterNode:

    def __init__(self):
        self.prev = set()
        self.next = set()


def _set_dict():
    all_letters = dict()

    for letter in list(string.ascii_lowercase):
        all_letters[letter] = LetterNode()

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
            for i in range(len(self.order)):
                self.order[i][word[i]].add(word[i])

