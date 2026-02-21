# Hangman in Python
import random

hangman_art = {0: ("     ", "     ", "     "),
               1: ("   o ", "     ", "     "),
               2: ("   o ", "   | ", "     "),
               3: ("   o ", "  /| ", "     "),
               4: ("   o ", "  /|\\", "     "),
               5: ("   o ", "  /|\\", "  /  "),
               6: ("   o ", "  /|\\", "  / \\")}

words: tuple = ('apple', 'bus', 'car', 'cat', 'dog', 'earth')
answer: str = random.choice(words)
hint: list = ['_'] * len(answer)        # the length of answer in underscores
bad_guess: int = 0
guessed = set()

while True:
    print("--------")
    for line in hangman_art[bad_guess]:        # bad_guess = hangman_art dictionary key 
        print(line)
    print("--------")
    print(" ".join(hint))
    guess: str = input("Enter a letter: ").lower() 

    if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

    if guess in guessed:
            print(f"{guess} is already guessed")
            continue

    guessed.add(guess)

    if guess in answer: 
        for i in range(len(answer)):
            if answer[i] == guess:
                hint[i] = guess        # correct guess replaces underscores

    else:
        bad_guess += 1 
    
    if "_" not in hint:
        print("--------")
        for line in hangman_art[bad_guess]:
            print(line)
        print("--------")
        print(" ".join(answer))
        print("YOU WIN!")
        break

    elif bad_guess >= len(hangman_art) - 1:
        print("--------")
        for line in hangman_art[bad_guess]:
            print(line)
        print("--------")
        print(" ".join(answer))
        print("YOU LOSE!")
        input("Press Enter to exit")
        break
