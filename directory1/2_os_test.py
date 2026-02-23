import os


choices = {
    "easy":   (10, "easy_words.txt"),
    "medium": (7,  "regular_words.txt"),
    "hard":   (5,  "hard_words.txt"),
}

response = input("choose easy regular hard: ")
max_wrong, wordfile = choices[response]

print(os.listdir())