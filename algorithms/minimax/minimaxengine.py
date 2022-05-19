import wordset.wordset as ws
import random


class Minimax:

    def __init__(self):
        self.wordset = list(ws.WordSet().get_solutions())
        self.yellow_letter = set()
        self.green_letter = set()
        self.black_letter = set()

    def next_word(self, goal):
        pass

    def add_info(self, exact, close, impossible):
        pass
