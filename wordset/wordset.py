import random
from pathlib import Path


class WordSet:

    def __init__(self):
        self._dictionary = set()

        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'possiblewords.txt'
        with open(file_location, 'r') as file:
            lines = file.readlines()

        file.close()

        for word in lines:
            self._dictionary.add(word[0:5])

    def get_dictionary(self):
        return self._dictionary

    def get_random_word(self):
        return random.choice(tuple(self._dictionary))
