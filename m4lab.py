import random

while True:

    roll = 0
    draw = 0
    userWin = 0
    compWin = 0

    user = input("press y to play rolling dice, or any other key to quit:")

    if user.lower() == "y":

        while roll < 5:

            userDiceRoll = random.randint(1, 6)
            compDiceRoll = random.randint(1, 6)


            if userDiceRoll == compDiceRoll:
                print("Draw no winner!", userDiceRoll, "vs", compDiceRoll)
                draw += 1

            elif userDiceRoll < compDiceRoll:
                print("Computer wins!", userDiceRoll, "vs", compDiceRoll)
                compWin += 1

            elif userDiceRoll > compDiceRoll:
                print("User wins!", userDiceRoll, "vs", compDiceRoll)
                userWin += 1

            roll += 1

            if roll == 5:
                print("")
                print("Reporting the results:")
                print("Total number of dice rolls:" + str(roll))
                print("The user won:", userWin, "times")
                print("The computer won:", compWin, "times")
                print("The draw were:", draw, "times")
                break

    else:
        print("Exiting the game.")
        break

