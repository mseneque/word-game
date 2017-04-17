"""
Name:  Matthew Seneque
Student Number: 10401788

Word-Game
"""


import random


# Create a list of 100 words that are similar enough to work well for this game
candidateWords = ['AETHER', 'BADGED', 'BALDER', 'BANDED', 'BANTER', 'BARBER',
                  'BASHER', 'BATHED', 'BATHER', 'BEAMED', 'BEANED', 'BEAVER',
                  'BEDDER', 'BEDELL', 'BEDRID', 'BEEPER', 'BEGGAR', 'BEGGED',
                  'BELLES', 'BENDED', 'BENDEE', 'BETTER', 'BLAMER', 'BLOWER',
                  'BOLDER', 'BOLTER', 'BOMBER', 'BOOKER', 'BOPPER', 'BORDER',
                  'BUDGER', 'BUMPER', 'BUSHER', 'BUSIER', 'CEILER', 'DEADEN',
                  'DELVER', 'DENSER', 'DEXTER', 'EVADER', 'GELDED', 'GELDER',
                  'HERDER', 'HIDDEN', 'JESTER', 'JUDDER', 'KIDDED', 'KIDDER',
                  'LEASER', 'LEVIED', 'LEVIER', 'LEVIES', 'LIDDED', 'MADDER',
                  'MINDER', 'NEATER', 'NEEDED', 'NESTER', 'PENNER', 'PERTER',
                  'PONDER', 'RADDED', 'REALER', 'REAVER', 'REEDED', 'REIVER',
                  'SEARER', 'SEDGES', 'SEEDED', 'SEISER', 'SETTER', 'SIDDUR',
                  'TENDER', 'TERMER', 'VENDER', 'WEDDER', 'WEEDED', 'WELDED',
                  'BOTHER', 'BOWYER', 'BRACER', 'DEARER', 'HEIFER', 'LEAPER',
                  'PODDED', 'RENDER', 'TEMPER', 'BECKET', 'BELIES', 'BOBBER',
                  'BOSKER', 'DEAFER', 'HEARER', 'LEANER', 'MEANER', 'PEWTER',
                  'RELIER', 'TEENER', 'YONDER', 'MENDER']


# -- getDificulty --
# Prompts the user to input their preferred difficulty
# Inputs: none
# Outputs: returns a single integer value.
def getDifficulty():
    levels = {1: 'easy', 2: 'medium', 3: 'hard', }
    while True:
        for key, level in levels.items():
            print('\t   ', key, '-', level)
        try:
            difficulty = int(input('\n\tEnter a difficulty level: '))
            if difficulty in levels:
                break
        except ValueError:
            pass
    return(difficulty)


# -- Play --
# Plays the game with integer inupt for difficulty,
# easy->1, medium->2 or hard->3.
# Inputs: difficulty as integer default is 2
#         listsize as integer default is 6
#         guessesLeft as integer default is 6
# Outputs: none
def play(difficulty=2, listsize=6, guessesLeft=6):
    won = False
    matchHistory = {}
    guessesLeft = guessesLeft - difficulty
    listsize = listsize + difficulty

    wordList = random.sample(candidateWords, listsize)
    password = random.choice(wordList)

    print('\n\tWelcome to the Guess-The-Word Game.\n\tPassword is one of these words:\n')

    while won is False and guessesLeft > 0:
        for key, word in list(enumerate((wordList), start=1)):
            import pdb; pdb.set_trace()  # breakpoint 3e590f59 //

            # Print example: "1) BECKET"
            print('\t  ', key, ') ', word, end='  ', sep='')

            # If word has been previously guessed let the user know correct matches.
            # Print example: "[2/6 correct]"
            if matchHistory.get(key) is not None:
                print('[', matchHistory[key], '/', len(word), ' correct]', end='', sep='')
            print('')

        print('\n\tGuesses remaining:', guessesLeft)

        try:
            guess = int(input('\tGuess (enter 1-' + str(listsize) + '): '))
        except ValueError:
            continue

        # Error checking for invalid integer range
        if guess < 1 or guess > (listsize):
            continue

        guessesLeft -= 1
        print('\n\n')

        matches = compareWords((wordList[guess - 1]), password)
        if matches is len(password):
            won = True

        if won:
            print('\t"', password, '" - password correct\n\n', sep='')
            break
        else:
            print('\tPrevious guess "', wordList[guess - 1], '" is incorrect\n\n', sep='')

        matchHistory[guess] = matches

    print('\tYou win\n\n' if won else '\tYou lose\n\n')
    return()


# -- compareWords --
# Receives two strings and returns the number of matching characters between them.
# Inputs: word1 as string
#         word2 as string
# Outputs: returns a single integer value
def compareWords(word1, word2):
    return len(set(enumerate(word1)).intersection(enumerate(word2)))


# Starts the game.
while True:
    play(getDifficulty())
    choice = (input("\n\tPress 'y' to play again:"))
    if str.lower(choice) != 'y':
        break
