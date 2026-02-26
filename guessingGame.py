import random

def GuessingGame():
    guess = random.randint(1,10)
    while True:
        print("Enter your Guess :")
        num = int(input())
        if num == guess:
            return f"You guessed correct {guess}"
            break
        elif num < guess:
            print("Low")
        elif num > guess:
            print("High")
        else:
            print("Guess in between 1 and 10")

print(GuessingGame())