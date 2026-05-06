import random

words = ["laptop", "keyboard", "shinchan", "internet", "secret"]
word = random.choice(words)

guessed_word = ["_"] * len(word)
attempts = 6

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed_word:
    print("\nWord:", " ".join(guessed_word))
    guess = input("Enter a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

if "_" not in guessed_word:
    print("You won! 🎉 The word was:", word)
else:
    print("You lost 😢 The word was:", word)