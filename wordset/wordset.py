from pathlib import Path

class wordset:

    def __init__(self):
        script_location = Path(__file__).absolute().parent
        file_location = script_location / 'possiblewords.txt'
        with open(file_location, 'r') as file:
            lines = file.readline()

        print(lines)

wordset()