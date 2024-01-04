# Hangman Game

# Import necessary modules
import random
from hangman_words import word_list
from hangman_art import logo, stages

# Select a random word from the word list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Set the initial number of lives
lives = 6

# Initialize end_of_game flag
end_of_game = False

# Print the Hangman game logo
print(logo)

# Initialize the display with underscores for each letter in the chosen word
display = ["_" for _ in range(word_length)]

# Main game loop
while not end_of_game:
    # Get a letter guess from the player
    guess = input("Guess a letter: ").lower()

    # Check if the guessed letter has already been guessed
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check if the guessed letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    # If the guessed letter is not in the chosen word, decrement lives
    if guess not in chosen_word:
        print(f"{guess} is not in the word.")
        lives -= 1

        # If no lives remaining, end the game and print a losing message
        if lives == 0:
            end_of_game = True
            print("You lose!")

    # Print the current state of the word display
    print(f"{' '.join(display)}")

    # Check if all letters have been guessed, end the game and print a winning message
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Print the current Hangman stage
    print(stages[lives])
