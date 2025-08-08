x = int(input('Enter the maximum value for the range at which the computer selects its number from:'))

guesses = int(input('How many guesses would you like?'))
#  user choses range for computer (0-x)

numlist = []
for i in range(x):
    numlist.append(i)
numlist.append(x)
#  list is created with the range of numbers from 0 to the value input

# import random, assign y as computers random number
import random
y = random.choice(numlist)

i = 0
while i<guesses:
    z = int(input('Guess the computers number:'))
    if z == y:
        print('You win! The number was ' + str(y))
        i = guesses
    elif z < y:
        print('Too Low!')
        i += 1
        if i == guesses:
            print('You Lose! The number was ' + str(y))
    elif z > y:
        print('Too High!')
        i += 1
        if i == guesses:
            print('You Lose! The number was ' + str(y))

