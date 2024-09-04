import random

# List of words for the game
words = ['python', 'development', 'hangman', 'challenge', 'programming', 'computer', 'artificial', 'intelligence']

def select_word():
    """Select a random word from the list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_hangman():
    word = select_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print(f"Good guess! {guess} is in the word.")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            guessed_letters.add(guess)
            print(f"Wrong guess! {guess} is not in the word.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame over! The word was: {word}")

# Run the game
if __name__ == "__main__":
    play_hangman()
