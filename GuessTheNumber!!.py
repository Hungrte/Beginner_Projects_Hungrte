import random

randomNum = random.randint(1, 20)
tries = 0

while True:
    tries += 1
    answer = int(input("Guess a number between 1 and 20: "))
    
    if answer == randomNum:
        print("Congratulations! You guessed the correct number:", randomNum)
        print("you guessed it in", tries, "attempts!")
        break

    if answer < randomNum:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    
    
