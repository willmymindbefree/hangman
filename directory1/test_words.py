# Test script to print hangman word files

difficulties = ['easy', 'regular', 'hard']

for difficulty in difficulties:
    print(f"\n{'='*50}")
    print(f"{difficulty.upper()} WORDS")
    print('='*50)
    
    try:
        with open(f'{difficulty}_words.txt', 'r') as file:
            words = file.read().splitlines()
            print(f"Total words: {len(words)}")
            print(f"Words: {words[:10]}{'...' if len(words) > 10 else ''}")
    except FileNotFoundError:
        print(f"Error: {difficulty}_words.txt not found")
