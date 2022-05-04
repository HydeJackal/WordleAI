import algorithms.trie.trie as tr
import wordset.wordset as ws


class TrieEngine:

    def __init__(self):
        words = ws.WordSet()
        tr.Trie(words.get_solutions())
