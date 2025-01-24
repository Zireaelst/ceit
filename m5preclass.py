import random

def rolldice():
    face = random.randint(1,7)
    return face

while True:
    nDouble = 0

    maxRounds = input("How many rounds do you want to do?(ENTER to quit):")

    if maxRounds == "":
        break

    try:
        maxRounds = int(maxRounds)
    except:
        print("Please enter an number")
        continue

    for round in range(0,maxRounds):
        die1 = rolldice()
        die2 = rolldice()

        if die1 == die2:
            nDouble += 1

    percent = (nDouble/maxRounds)*100
    print("Out of", maxRounds, "you rolled", nDouble, "doubles, or ", percent, "%")

print("Thanks for playing!")
