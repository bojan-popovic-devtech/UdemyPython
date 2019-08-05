
import random

highest = 1000
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}: ".format(highest))


guess = int(input())
while guess != answer:
    if guess < answer:
        print("Please guess higher")
        guess = int( input() )
    else:  # guess must be greater than number
        print("Please guess lower")
        guess = int( input() )
print("YOu guessed it correctly")