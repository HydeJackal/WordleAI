import string
import random
from collections import Counter
import collections

def find_dup_char(input):
    WC = Counter(input)
    j = -1
    for i in WC.values():
        j = j + 1
        if( i > 1 ):
            print WC.keys()[j]

def isUniqueChars(string):
 
    freq = Counter(string)
 
    if(len(freq) == len(string)):
        return True
    else:
        return False

def indexes(my_list, desired_element):
    return [index for index, element in enumerate(my_list) if element == desired_element]

def run_rand(): 
  f = open('/Users/rishabhprakash/Desktop/Cornell/Spring2022/CS4701/WordleAI/wordset/possiblesolutions.txt', 'r')
  g = open('/Users/rishabhprakash/Desktop/Cornell/Spring2022/CS4701/WordleAI/wordset/possibleguesses.txt', 'r')

  solutionlist = f.read().splitlines()
  guesslist = g.read().splitlines()
  guesses = 1
  curr_guess = "crane"
  feedback = raw_input("Enter your feedback: ")

  while (feedback != "ggggg"): 
    solutionlist.remove(curr_guess)

    if (isUniqueChars(curr_guess) == False):
      
      d = collections.defaultdict(int)
      for c in curr_guess:
        d[c] += 1

      key_list = list(d.keys())
      val_list = list(d.values())
      position = val_list.index(2)
      repeated_indices = indexes(list(curr_guess), key_list[position])

      if (feedback[repeated_indices[0]] == "g" and feedback[repeated_indices[1]] == "g"):
        solutionlist = [solution for solution in solutionlist if solution[repeated_indices[0]] == curr_guess[repeated_indices[0]] 
        and solution[repeated_indices[1]] == curr_guess[repeated_indices[1]]]

      elif (feedback[repeated_indices[0]] == "g" and feedback[repeated_indices[1]] == "y"):
        solutionlist = [solution for solution in solutionlist if solution[repeated_indices[0]] == curr_guess[repeated_indices[0]] 
        and solution[repeated_indices[1]] != curr_guess[repeated_indices[1]] and solution.count(curr_guess[repeated_indices[1]]) == 2]
      
      elif (feedback[repeated_indices[0]] == "y" and feedback[repeated_indices[1]] == "g"):
        solutionlist = [solution for solution in solutionlist if (solution[repeated_indices[1]] == curr_guess[repeated_indices[1]] 
        and solution[repeated_indices[0]] != curr_guess[repeated_indices[0]] and solution.count(curr_guess[repeated_indices[1]]) == 2)]
      
      elif (feedback[repeated_indices[0]] == "g" and feedback[repeated_indices[1]] == "b"):
        solutionlist = [solution for solution in solutionlist if solution[repeated_indices[0]] == curr_guess[repeated_indices[0]] 
        and solution[repeated_indices[1]] != curr_guess[repeated_indices[1]] and solution.count(curr_guess[repeated_indices[1]]) == 1]
      
      elif (feedback[repeated_indices[0]] == "b" and feedback[repeated_indices[1]] == "g"):
        solutionlist = [solution for solution in solutionlist if solution[repeated_indices[1]] == curr_guess[repeated_indices[1]] 
        and solution[repeated_indices[0]] != curr_guess[repeated_indices[0]] and solution.count(curr_guess[repeated_indices[1]]) == 1]
      
      for i in range(0, 5):
        if (i != repeated_indices[0] and i != repeated_indices[1]):
          if (feedback[i] == "b"):
            solutionlist = [solution for solution in solutionlist if curr_guess[i] not in solution]
          if (feedback[i] == "y"):
            solutionlist = [solution for solution in solutionlist if curr_guess[i] in solution and curr_guess[i] != solution[i]]
          if (feedback[i] == "g"):
            solutionlist = [solution for solution in solutionlist if solution[i] == curr_guess[i]]
      
      for solution in solutionlist:
        print(solution)
      
      next_guess = random.choice(solutionlist)  
      print("Suggested next guess is: " + next_guess)
      curr_guess = next_guess
      guesses+=1
      feedback = raw_input("Enter your feedback: ")

    else :
      for i in range(0, 5):
        if (feedback[i] == "b"):
          solutionlist = [solution for solution in solutionlist if curr_guess[i] not in solution]
        if (feedback[i] == "y"):
          solutionlist = [solution for solution in solutionlist if curr_guess[i] in solution and curr_guess[i] != solution[i]]
        if (feedback[i] == "g"):
          solutionlist = [solution for solution in solutionlist if solution[i] == curr_guess[i]]

      for solution in solutionlist:
        print(solution)

      next_guess = random.choice(solutionlist)  
      print("Suggested next guess is: " + next_guess)
      curr_guess = next_guess
      guesses+=1
      feedback = raw_input("Enter your feedback: ")

  print("Solved in " + str(guesses) + " guesses!")
  

run_rand()