
<<<<<<< HEAD
import random

def hangman():
    word_list = ["Python", "Tesla", "Chihuahua", "Chicken", "Hangman"]
    random_number = random.randint(0, 4)
    word = word_list[random_number]
    wrong_guesses = 0
=======
def hangman(word):
    wrong = 0 # keeps track of how many wrong guesses
>>>>>>> 534c683e32f8e2a3928d2cc3eea46292e5d85eb9
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
<<<<<<< HEAD
             "|               ",
             "|               "
              ]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman!')

    while wrong_guesses < len(stages) - 1:
        print('\n')
        guess = input("Guess a letter: ")
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess)
            letter_board[character_index] = guess
            remaining_letters[character_index] = '$'
        else:
            wrong_guesses += 1
        print((' '.join(letter_board)))
        print('\n'.join(stages[0: wrong_guesses + 1]))
        if '__' not in letter_board:
            print('You win! The word was:')
            print(' '.join(letter_board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0: wrong_guesses]))
        print('You lose! The words was {}'.format(word))

hangman()
=======
             "|               "
              ]
    rletters = list(word) # variable rletters contain each char in the variable word that keeps track of which letters are left to guess.
    board = ["__"] * len(word) # variable board is a list of strings used to keep track of hints displayed
    win = False
    print("Welcome to Hangman!")
    # the loop and game continues as long as variable wrong is less than len(stages) - 1.
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter "
        char = input(msg)
        if char in rletters:
            cind = rletters \
                   .index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n"
              .join(stages[0: e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n"
              .join(stages[0: \
              wrong]))
        print("You lose! It was {}."
              .format(word))

hangman("cat")
>>>>>>> 534c683e32f8e2a3928d2cc3eea46292e5d85eb9
