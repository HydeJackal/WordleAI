import algorithms.trie.trieengine as te
import wordlegame as wg
import time


def run_all(iterate):
    engines = {'Trie': te.TrieEngine()}

    for engine in engines.keys():
        print('Test for ' + str(engine) + ' :')
        won = 0
        guessed_won = 0
        total_guesses = 0
        state = wg.WordleGame()

        start = time.time()
        for _ in range(iterate):
            algo = engines[engine]
            result = state.play_game(algo)
            if result[0]:
                won += 1
                guessed_won += result[1]
            total_guesses += result[1]

        end = time.time()
        print('Total time for ' + str(iterate) + ' iterations: ' + str(end - start))
        print('Proportion of games won: ' + str(won / iterate))
        print('Average number of guesses in games won: ' + str(guessed_won / won))
        print('Average number of guesses in all games: ' + str(guessed_won / won))
        print()
    print('End of tests.')


