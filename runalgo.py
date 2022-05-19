import algorithms.trie.trieengine as te
import algorithms.randomized.randomizedengine as re
import algorithms.entropy.entropyengine as en
import wordlegame as wg
import time


def run_all(iterate):
    engines = {'Random': re.Randomized
               }

    for engine in engines.keys():
        print('Test for ' + str(engine) + ' :')
        won = 0
        guessed_won = 0
        total_guesses = 0
        state = wg.WordleGame()
        guessCount = list()
        start = time.time()
        for _ in range(iterate):
            state = wg.WordleGame()
            algo = engines[engine]
            result = state.play_game(algo)
            if result[0]:
                won += 1
                guessCount.append(result[1])
                guessed_won += result[1]
            total_guesses += result[1]

        end = time.time()
        print('Total time for ' + str(iterate) + ' iterations: ' + str(end - start))
        print('Number of games won: ' + str(won))
        print('Maximum number of guesses: ' + str(max(guessCount)))
        print('Minimum number of guesses: ' + str(min(guessCount)))
        print('Proportion of games won: ' + str(won / iterate))
        print('Average number of guesses in games won: ' + str(guessed_won / won))
        print('Average number of guesses in all games: ' + str(total_guesses / iterate))
        print('Guess Distribution: ')
        print('1: ' + str(guessCount.count(1)))
        print('2: ' + str(guessCount.count(2)))
        print('3: ' + str(guessCount.count(3)))
        print('4: ' + str(guessCount.count(4)))
        print('5: ' + str(guessCount.count(5)))
        print('6: ' + str(guessCount.count(6)))
        print()
    print('End of tests.')
