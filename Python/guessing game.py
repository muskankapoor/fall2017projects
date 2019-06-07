import random
secretNumber = random.randint(1, 20) #randomly selects a number for the game
print('I am thinking of a number between 1 and 20.')

for guesstaken in range(1, 7): #playger can take only six guesses
    print ('Guess a number:')
    number=int(input())
    
    if number > secretNumber: 
        print ('Guess too high')
    elif number < secretNumber:
        print ('Guess too low')
    else:
        break
    
if number==secretnumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))

