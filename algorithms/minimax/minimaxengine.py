import wordset.wordset as ws
import wordlegame as wg
import random


class Minimax:

  def __init__(self):
    self.wordset = list(ws.WordSet().get_solutions())
    self.yellow_letter = set()
    self.green_letter = set()
    self.black_letter = set()
    self.goal = str 


  def next_word(self, goal):

    self.goal = goal
    
    for letter in self.black_letter:
      self.wordset = [word for word in self.wordset if not letter in word]
    
    for letter, position in self.green_letter:
      self.wordset = [word for word in self.wordset if word[position] == letter]
    
    for letter, position in self.yellow_letter:
      self.wordset = [word for word in self.wordset if letter in word and word[position] != letter]

    size = 100000000
    for word in self.wordset:
      remaining_wset_size = self.get_remaining_wordset_size(word)
      if (remaining_wset_size < size): 
        size = remaining_wset_size
        return_word = word
  
    guess = return_word
    
    self.wordset.remove(guess)
    return guess


  def add_info(self, exact, close, impossible): 
      for position, letter in exact:
        self.green_letter.add((letter, position))
      
      for position, letter in close: 
        self.yellow_letter.add((letter, position))
      
      for letter in impossible: 
        self.black_letter.add(letter)


  def get_remaining_wordset_size(self, word):
    wordset = self.wordset
    
    feedback_str = ""
    for i in range(5):
      if (word[i] == self.goal[i]):
        feedback_str+="g"
      elif (word[i] not in self.goal):
        feedback_str+="b"
      elif (word[i] in self.goal and word[i] != self.goal[i]):
        feedback_str+="y"

    for i in range(5):
      if feedback_str[i] == "g":
        wordset = [word for word in wordset if word[i] == self.goal[i]]
      if feedback_str[i] == "b":
        wordset = [word for word in wordset if word not in self.goal]
      if feedback_str[i] == "y":
        wordset = [word for word in wordset if word in self.goal and word[i] != self.goal[i]]

    return len(wordset)


