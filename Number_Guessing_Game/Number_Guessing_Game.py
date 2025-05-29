from random import randint

answer = randint(1, 100)


count = 1


while True:
    try:
        guess = int(input('Please guess a number between 1 and 100: '))
        if guess < answer:
            print('Too low, try again!')
            count += 1
        elif guess > answer:
            print('Too high, try again!')
            count += 1
        else:
            print('Congratulations! You found the number')
            print(f'Number of guesses: {count}') 
            break
    except ValueError:
        print('Invalid input. Please enter a valid number')             
