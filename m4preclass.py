import random
max_guesses = 10
max_range = 40
print("Welcome to guessing game!")
print("Guess number between 1 and" , max_range)
print("You will have" , max_guesses , "guesses")

def playOneRound():
    target = random.randint(1, max_range)
    guessCounter = 0

    while True:
        userGuess = input("Guess a number: ")
        try:
            guess = int(userGuess)
        except:
            print("You need to enter a number")
            continue

        guessCounter += 1

        if guess == target:
            print("You got it")
            print("It only took" , guessCounter, "guesses")
            break

        elif guess < target:
            print("Your guess is too low")

        else:
            print("Your guess is too high")

        if guessCounter == max_guesses:
            print("Sorry, you did not guess correctly in" , guessCounter, "guesses")
            print("The number was:", target)
            break

while True:
    playOneRound()
    goAgain = input("Would you like to play again? (Press ENTER to continue, or q to quit)")

    if goAgain.lower() == "q":
        break

print("Thanks for playing!")


