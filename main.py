import random

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

name = input("What's your name: ")
print("Good Luck!", name)
use_own_word = input("Do you want to guess your own word? (yes/no): ").lower()

if use_own_word == 'yes':
    word = input("Enter your word (it should be in the list to play properly): ").lower()
    if word not in words:
        print(f"Warning: '{word}' is not in the default word list. The game will still continue.")
else:
    word = random.choice(words)

print("\nGuess the characters of the word!")

guesses = ''
turns = 4

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1

    if failed == 0:
        print("\nYou win! 🎉")
        print("The word is:", word)
        break

    print()
    guess = input("Guess a character: ").lower()
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong ❌")
        print(f"You have {turns} more guesses\n")

        if turns == 0:
            print("You Lose 😢")
            print("The word was:", word)
