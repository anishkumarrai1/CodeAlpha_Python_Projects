"""
CodeAlpha Python Internship - Task 1: Hangman Game
A simple text-based Hangman game using a predefined word list.
"""

import random
# Predefined list of 5 words (no file/API needed)
WORDS = ["python", "hangman", "internship", "programming", "computer", "coading", "maharaj", "rajshree","anime","superman","bottle"]

MAX_WRONG_GUESSES = 6

HANGMAN_PICS = [
    """
      ------
      |    |
      |
      |
      |
      |
    --------
    """, 
    """
      ------
      |    |
      |    O
      |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |    |
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   /
      |
    --------
    """,
    """
      ------
      |    |
      |    O
      |   /|\\
      |   / \\
      |
    --------
    """,
]


def choose_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0

    print("=" * 40)
    print("  WELCOME TO HANGMAN")
    print("=" * 40)
    print(f"Guess the word! You have {MAX_WRONG_GUESSES} wrong attempts allowed.\n")

    while wrong_guesses < MAX_WRONG_GUESSES:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {MAX_WRONG_GUESSES - wrong_guesses}")
        print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "None")

        # Check win condition
        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            break

        guess = input("\nEnter a letter: ").strip().lower()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print(">> Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print(">> You already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f">> Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f">> Wrong! '{guess}' is not in the word.\n")

    # Final check after loop ends (loss condition)
    if wrong_guesses == MAX_WRONG_GUESSES:
        print(HANGMAN_PICS[wrong_guesses])
        print(f"\n💀 Game Over! You've run out of guesses. The word was: '{word}'")


def main():
    while True:
        play_hangman()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()
