import random
import string

# List of words for the game
WORDS = ["python", "computer", "programming", "database", "algorithm", "science", "network", "developer"]

def choose_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)

def display_progress(word, guessed_letters):
    """Shows the current word progress with guessed letters revealed."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def get_valid_guess(guessed_letters):
    """Ensures valid single-letter input and prevents duplicate guesses."""
    while True:
        guess = input("\nGuess a letter: ").strip().lower()

        if len(guess) == 1 and guess in string.ascii_lowercase and guess not in guessed_letters:
            return guess
        elif guess in guessed_letters:
            print("You've already guessed that letter!")
        else:
            print("Invalid input! Please enter a single letter.")

def hangman():
    """Main game loop that manages user interactions, guesses, and game logic."""
    word = choose_word()  # Select a word randomly
    word_letters = set(word)  # Unique letters in the word
    guessed_letters = set()  # Letters guessed by the user
    lives = 6  # Maximum incorrect guesses allowed

    print("\n>>> Welcome to Hangman!")
    print(display_progress(word, guessed_letters))  # Show initial empty state

    while len(word_letters) > 0 and lives > 0:
        print(f"\nYou have {lives} lives left.")
        print(f"Letters guessed: {' '.join(sorted(guessed_letters))}")
        print("Word progress:", display_progress(word, guessed_letters))

        guess = get_valid_guess(guessed_letters)  # Get user's guess
        guessed_letters.add(guess)

        if guess in word_letters:
            word_letters.remove(guess)  # Correct guess removes letter
        else:
            lives -= 1  # Incorrect guess reduces lives
            print("Wrong guess! That letter is not in the word.")

    # End-game messages
    if lives == 0:
        print(f"\nGame Over! The word was **{word.upper()}**.")
    else:
        print(f"\nCongratulations! You guessed the word **{word.upper()}**.")

# Run the game
if __name__ == "__main__":
    hangman()
