# Guess the number
from random import randint

# Default number range
minnum = 1
maxnum = 10

# Generate random number in the given range
num = randint(minnum, maxnum)

# Set the starting number of tries
tries = 1
maxtries = 3

def print_tries():
    print('Tries ' + str(tries) + ' / ' + str(maxtries))

while tries == 1:
    print(num)
    raw_guess = input('Guess a nubmer between ' + str(minnum) + ' and ' + str(maxnum) + '\n')

    # Get into the settings to change the numberrange 
    if raw_guess == 'settings':
        print('In the settings')
        minnum = int(input('Set the min num: '))
        maxnum = int(input('Set the max num: '))
        maxtries = int(input('Set the max tries: '))
        num = randint(minnum, maxnum)
        tries = 1

    if raw_guess.isdigit():
        guess = int(raw_guess)
        break

while tries < maxtries:
    print_tries()
    if guess == num:
        print('Spot on! Congratz')
        print('You guessed it in ' + str(tries) + ' tries')
        break
    
    tries += 1

    if guess > num:
        print('Too high. Try again')
    elif guess < num:
        print('Too low. Try again')

    guess = int(input('New guess: '))


if not tries < maxtries: 
    print('Out of tries. The number was ' + str(num))