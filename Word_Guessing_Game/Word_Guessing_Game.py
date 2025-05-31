import random


# Create a random_word with words.txt
with open("words.txt", "r") as file:
    content = file.read()
word_list = content.strip().split(',')
word = random.choice(word_list)

# Define the nomber of guesses
guesses = 7

# Input a guess
guess = input(f"Try to guess the word, you have {guesses} guesses reamining: ")

# Count the numbers of guesses and initialise the result
count = 0
result = ''

# Loop to compare guess and word
while count < 7:
    if guess == word:
        print(f'Congratulations! You find the word in {count + 1} guesses')
        break
    for i in range(len(word)):
        if guess[i] == word[i]:
            result += guess[i]
        else:
            result += "_"
    count += 1
    print('Result:', result)
    result = ''
    if count == 7:
        print(
            f"Sorry, you don't have guesses remaining... The word was {word}")
        break
    guess = input(f"Try again, you have {guesses - count} guesses remaining: ")
