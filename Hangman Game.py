import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word_list = ["aardvark", "baboon", "camel", "jazz", "grass", "follow", "castle", "cloud"]

chosen_word = list(random.choice(word_list))
blank_list = ["_" for _ in chosen_word]

incorrect_guesses = 0

def display_game():
    """
    Displays the current state of the game.
    """
    print(HANGMANPICS[incorrect_guesses])
    print("Current word: " + " ".join(blank_list))

def make_a_guess(guess):
    """
    Handles user guesses.
    """
    global incorrect_guesses
    correct_guess = False

    for idx, letter in enumerate(chosen_word):
        if guess.lower() == letter:
            blank_list[idx] = guess.lower()
            correct_guess = True

    if not correct_guess:
        print(f"There is no '{guess}', sorry.")
        incorrect_guesses += 1


print(" Welcome to Hangman!")
display_game()

while incorrect_guesses < 6:
    if blank_list == chosen_word:
        print("\n YOU WIN! The word was: " + "".join(chosen_word))
        break

    guess = input("\nMake a guess: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue

    if guess in blank_list:
        print("You already guessed that letter.")
        continue

    make_a_guess(guess)
    display_game()

if incorrect_guesses == 6:
    print("\n GAME OVER! The word was: " + "".join(chosen_word))