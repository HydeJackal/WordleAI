import wordset.wordset as ws

from colorama import init, Fore, Back, Style, deinit, reinit


class WordleGame:

    def __init__(self, possible_words):
        self._ws = ws.WordSet()
        self._all_words = possible_words.get_dictionary()
        self._goal = self._ws.get_random_word()

    def play_game(self, engine=None):
        self.new_random_word()
        guessed_words = list()

        if not engine:
            init(autoreset=True)
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'Welcome to Wordle!')
            deinit()

        while len(guessed_words) < 6 and self._goal not in guessed_words:
            if engine:
                guessed_words.append(engine.new_word())
            else:
                self._wordle_format_ui(guessed_words)
                guessed_words = self._wordle_guessing_ui(guessed_words)

        if not engine:
            reinit()
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'Game End! Word was ' + self._goal + '.')
            deinit()
            self._wordle_format_ui(guessed_words, True)

        return self._goal in guessed_words, len(guessed_words)

    def new_random_word(self):
        self._goal = self._ws.get_random_word()

    def _wordle_format_ui(self, guessed, end=False):
        reinit()
        for word in guessed:
            for j, letter in enumerate(word):
                if letter == self._goal[j]:
                    print(Back.LIGHTGREEN_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + ' ' + letter + ' ', end=' ')
                elif letter in self._goal:
                    print(Back.LIGHTYELLOW_EX + Fore.LIGHTWHITE_EX + Style.BRIGHT + ' ' + letter + ' ', end=' ')
                else:
                    print(Back.WHITE + Fore.LIGHTWHITE_EX + Style.BRIGHT + ' ' + letter + ' ', end=' ')

            print()

        if not end:
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                  'You currently have ' + str(len(guessed)) + ' guesses.')
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                  'Input your next guess: ', end='')
            deinit()

    def _wordle_guessing_ui(self, guessed):
        new_guess = input().lower()

        while (len(new_guess) != 5 or
               not new_guess.isalpha() or
               new_guess in guessed or
               new_guess not in self._all_words):
            reinit()
            if len(new_guess) != 5:
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'Word must be of length five!')
            if not new_guess.isalpha():
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'Word must be made of alphabetical letters!')
            if new_guess in guessed:
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'Word cannot have been guessed already!')
            if new_guess not in self._all_words:
                print(Back.RED + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                      'World must be a valid word!')

            deinit()
            print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT +
                  'Invalid input. Please input a valid guess:', end='')
            new_guess = input().lower()

        guessed.append(new_guess)

        return guessed

    def get_word(self):
        return self._goal

    def get_possible_words(self):
        return self._all_words
