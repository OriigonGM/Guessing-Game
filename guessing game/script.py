import random

def guess():
    answer = random.randint(1, 100)
    guess = 0
    print("Guess a number between 1-100!")
    while guess != answer:
        guess = int(input(""))
        if guess < answer:
            print('Too low! Guess again!')
        elif guess > answer:
            print('Too high! Guess again!')
    print('Yay! You got it right!')
    playAgain()

def playAgain():
    re = input('Would you like to play again? "y" for yes and "n" for no.\n')
    if re == 'y':
        guess()
    elif re == 'n':
        quit
guess()