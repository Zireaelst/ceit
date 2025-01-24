import random


while True:

    userDiceRoll = input("Enter dice roll as a number between 1 and 6:")

    try:
        userDiceRoll = int(userDiceRoll)
        if not (1 <= userDiceRoll <= 6):
            print("Please enter a number between 1 and 6.")
            continue

    except ValueError:
        print("Please enter a number")
        continue


    compDiceRoll = random.randint(1,6)
    if userDiceRoll < compDiceRoll:
        print("user:", userDiceRoll, "computer:", compDiceRoll)
        print("Computer wins!")

    elif userDiceRoll > compDiceRoll:
        print("user:", userDiceRoll, "computer:", compDiceRoll)

        print("User wins!")

    else:
        print("user:", userDiceRoll, "computer:", compDiceRoll)

        print("It's a tie!")


    if input("Do you want to play again?(If you want to quit type 'n')").lower() == "n":
        print("Thank you for playing!")
        break




