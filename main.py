import random
from random_word import RandomWords

# Create an instance of the RandomWords class
r = RandomWords()

# Define the maximum number of attempts
MAX_ATTEMPTS = 6

def hangman():
    # Generate a random word
    word = r.get_random_word().lower()

    # Initialize the game state
    word_state = ['_' for _ in range(len(word))]
    attempts_left = MAX_ATTEMPTS
    used_letters = []

    # Main game loop
    while True:
        # Display the current game state
        print('\n' + ' '.join(word_state))
        print(f'Attempts left: {attempts_left}')
        print(f'Used letters: {used_letters}')

        # Prompt the user to enter a letter
        letter = input('Enter a letter: ').lower()

        # Validate the input
        if len(letter) != 1 or not letter.isalpha():
            print('Invalid input! Please enter a single letter.')
            continue
        elif letter in used_letters:
            print(f'You already used the letter "{letter}"! Please enter a different letter.')
            continue

        # Update the game state
        used_letters.append(letter)
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    word_state[i] = letter
        else:
            attempts_left -= 1

        # Check if the game is over
        if '_' not in word_state:
            print('Congratulations, you won!')
            print(f'The word was "{word}".')
            break
        elif attempts_left == 0:
            print('Game over, you lost!')
            print(f'The word was "{word}".')
            break

hangman()
