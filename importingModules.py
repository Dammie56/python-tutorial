"""import random

for i in range(6):
    print(random.randint(1, 15))"""

"""import sys
while True:
    print('Type exit to exit')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed exit!')"""

"""import sys
while True:
    print("You want to exit? Yes or No!")
    response = input()
    if response != "Yes":
        continue
        sys.exit()
    print("You typed yes")"""

## A GUESS GAME
"""import random

secretNumber = random.randint(1, 20)
print("I am thinking a number between 1 and 20")
for guessesTaken in range(1, 7):
    print("Take a guess!")
    guess = int(input())
    if guess < secretNumber:
        print("your guess is too low")
    elif guess > secretNumber:
        print("Your guess is too high")
    else:
        break
    if guess == secretNumber:
        print("Good job! You guessed my number in " + str(guessesTaken) + "guesses!")
    else:
        print("Nope.The number i was thinking of was " + str(secretNumber))"""

import random

print("Welcome to the number guess game!")
count_number_of_tries = 1
guessNumber = random.randint(1, 10)
print("I am thinking a number between 1 and 10")
print("Take a guess")
guess = int(input("Please guess a number between 1 and 10: "))
while guessNumber != guess:
    print("Sorry wrong number")
if count_number_of_tries == 4:
    break
elif guess < guessNumber:
    print("Your guess is low")
else:
    print("Your guess ia high")
guess = int(input("Please try again"))
count_number_of_tries += 1
if guessNumber == guess:
    print("Welldone, you won!")
else:
    print("Sorry, you lose game over!")
    print(f"The number you needed to guess was", {guessNumber})
