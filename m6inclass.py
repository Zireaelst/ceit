import random

def generate_random_string(length):
  letters = "aaaaabcdeeeeefghiiiiijklmnooooopqrstuuuuuuvwxyz"
  result = ""
  for i in range(length):
    result += random.choice(letters)
  return result

# Generate a list of 10 random strings
words = []
for i in range(20):
  words.append(generate_random_string(random.randint(3, 7)))

vowels = ["a", "e", "i", "o", "u"]

while True:
    luckyLetter = input("Enter your lucky letter [a, e, i, o, u]:")
    unluckyLetter = input("Enter your unlucky letter [a, e, i, o, u]:")


    if luckyLetter in vowels and unluckyLetter in vowels and luckyLetter != unluckyLetter:
        break
    else:
        print("You need to choose different lucky letter and unlucky letter from the list ['a', 'e', 'i', 'o', 'u']")

index = -1
points = 0

while True:
    stepSize = int(input("Enter 1, 2, or 3 to move on:"))
    index += stepSize

    try:
        currentWord = words[index]
    except IndexError:
        print("You have reached the end of the list. Game over!")
        break

    wordLength = len(currentWord)
    print("Current word:", currentWord)

    if currentWord.startswith(luckyLetter) or currentWord.endswith(luckyLetter):
        points += wordLength
        print("Great! The word starts/ends with", luckyLetter,": +",wordLength, "points")
    if currentWord.startswith(unluckyLetter) or currentWord.endswith(unluckyLetter):
        points -= wordLength
        print("Oh no! The word starts/ends with", unluckyLetter,": -",wordLength, "points")

    luckyCount = currentWord.count(luckyLetter)
    unluckyCount = currentWord.count(unluckyLetter)
    if luckyCount > 0:
        points += luckyCount
        print("Great! The word contains", luckyLetter, ": +", luckyCount, "points")
    if unluckyCount > 0:
        points -= unluckyCount
        print("Oh no! The word contains", unluckyLetter, ": -", unluckyCount, "points")

    print("Current points:",points)

    if points < 0:
        print("The game ends, your point is less than 0.")
        break


