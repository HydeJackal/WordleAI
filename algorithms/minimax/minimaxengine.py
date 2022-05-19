import wordset.wordset as ws
import random

class Minimax: 

  def __init__(self):
    self.wordset = list(ws.WordSet().get_solutions())
    self.yellow_letter = set()
    self.green_letter = set()
    self.black_letter = set()


  def next_word(self, goal):

    for letter in self.black_letter:
      self.wordset = [word for word in self.wordset if not letter in word]
    
    for letter, position in self.green_letter:
      self.wordset = [word for word in self.wordset if word[position] == letter]
    
    for letter, position in self.yellow_letter:
      self.wordset = [word for word in self.wordset if letter in word and word[position] != letter]

    size = 1000000
    for word in self.wordset:

    guess = random.choice(self.wordset)
    self.wordset.remove(guess)
    
    return guess


  def add_info(self, exact, close, impossible): 
      for position, letter in exact:
        self.green_letter.add((letter, position))
      
      for position, letter in close: 
        self.yellow_letter.add((letter, position))
      
      for letter in impossible: 
        self.black_letter.add(letter)


  def size_of_narrowed_list(self, guess, goal):
    wordset = list(ws.WordSet().get_solutions())
    feedback_string = ""
    for i in range(5):
      if (guess[i] == goal[i]):
        feedback_string.append("g")
      elif (guess[i] in goal and guess[i] != goal[i]):
        feedback_string.append("y")
      elif (guess[i] not in goal):
        feedback_string.append("b")

    for i in range(5):
      if (feedback_string[i] == "b"):
        wordset = [word for word in wordset if not guess[i] in word]
      if (feedback_string[i] == "g"):
        wordset = [word for word in wordset if word[i] == guess[i]]
      if (feedback_string[i] == "y"):
        wordset = [word for word in wordset if guess[i] in word and word[i] != guess[i]]
      
      return len(wordset)


