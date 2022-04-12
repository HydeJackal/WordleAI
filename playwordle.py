import wordlegame

from colorama import init, Fore, Back, Style

if __name__ == '__main__':
    game = wordlegame.WordleGame()
    end_state, _ = game.play_game()

    init(autoreset=True)
    if end_state:
        print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'You Won!')
    else:
        print(Back.BLACK + Fore.LIGHTWHITE_EX + Style.BRIGHT + 'You Lost!')
