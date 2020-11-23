import random


def hangman():
    
    # Randomly selects a word from the list
    
    words = ["cake", "pie", "dessert"] # Careful, Python differentiates capital letters
    random_number = random.randint(0, 2)
    word = words[random_number]
    
    # A tracker of wrong guesses, remaining letters, a hangman drawing (stored in a list), and a letter board are defined 

    wrong_guesses = 0
    stages = ["", "________      ", "|      |      ", "|      0      ", "|     /|\     ", "|     / \     ", "|"]
    remaining_letters = list(word)
    letter_board = ["__"] * len(word)
    win = False
    print('Welcome to Hangman')


    while wrong_guesses < len(stages) - 1:
        print('\n') # It's a spaced line
        guess = input("Guess a letter")
        
        if guess in remaining_letters:
            character_index = remaining_letters.index(guess) #saves the index where the letter was found
            letter_board[character_index] = guess #substitutes the guessed letter in the  letterboard
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
