
import random

try:
    with open("gameData.txt", "r") as file:
        userData = file.readline().split(',')
        userName = userData[0]
        score = int(userData[1])
        nProblems = int(userData[2])
        nCorrect = int(userData[3])
except FileNotFoundError:
    userName = input("Enter your name: ")
    score = 0
    nProblems = 0
    nCorrect = 0

print(f"Welcome, {userName}!")
print(f"Your current score: {score}")

while True:
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    print(f"What is {num1} + {num2}?")
    answer = input("Your answer (or press Enter to quit): ")

    if answer == "":
        break

    nProblems += 1
    if int(answer) == num1 + num2:
        print("Yes, you got it!")
        score += 2
        nCorrect += 1
    else:
        print(f"No, the correct answer was {num1 + num2}")
        score -= 1

    print(f"Your score is now {score}.")

with open("gameData.txt", "w") as file:
    file.write(f"{userName},{score},{nProblems},{nCorrect}")

print(f"Goodbye, {userName}! Your final score is {score}.")
