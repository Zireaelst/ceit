import os
import random

def fileExists(filepath):
    return os.path.exists(filepath)

def mainMenu():
    print("\nWelcome to Spanish / English Dictionary")
    print("1 Add new entry")
    print("2 Translate to Spanish")
    print("3 Update an entry")
    print("4 Delete an entry")
    print("5 For see the report ")
    print("6 For take quiz")
    print("7 Quit")
    return input("What to do? ")

def newEntry():
    with open("data.txt", "a") as file:
        en = input("Enter the English word: ")
        span = input("Enter the Spanish word: ")
        file.write(f"{en},{span}\n")

def translate():
    if not fileExists("data.txt"):
        print("Dictionary is empty. First add an entry.")
        return
    with open("data.txt", "r") as file:
        english_word_to_find = input("Enter the English word: ")

        line = file.readline()

        while line:
            english_word, spanish_word = line.strip().split(',')

            if english_word == english_word_to_find:
                print(f"{english_word} means {spanish_word} in Spanish.")
                break

            line = file.readline()

        if not line:
            print("Not found!")

def updateEntry():
    if not fileExists("data.txt"):
        print("Dictionary is empty. First add an entry.")
        return
    filepath = 'data.txt'
    english_word_to_update = input("Enter the English word to update: ")


    with open(filepath, 'r') as file:
        lines = file.readlines()

    found = False

    for i, line in enumerate(lines):
        english_word, spanish_word = line.strip().split(',')
        if english_word == english_word_to_update:
            new_spanish_word = input("Enter the new Spanish translation: ")
            lines[i] = f"{english_word},{new_spanish_word}\n"
            found = True
            break

    with open(filepath, 'w') as file:
        file.writelines(lines)

    if found:
        print("The translation has been updated.")
    else:
        print("Not found!")

def deleteEntry():
    if not fileExists("data.txt"):
        print("Dictionary is empty. First add an entry.")
        return
    filepath = 'data.txt'
    english_word_to_delete = input("Enter the English word to delete: ")

    with open(filepath, 'r') as file:
        lines = file.readlines()

    found = False

    updated_lines = []

    for line in lines:
        english_word, _ = line.strip().split(',')
        if english_word == english_word_to_delete:
            found = True
        else:
            updated_lines.append(line)

    with open(filepath, 'w') as file:
        file.writelines(updated_lines)

    if found:
        print("Translation is deleted.")
    else:
        print("Not found!")

def produceReport():
    if not fileExists("data.txt"):
        print("Dictionary is empty. First add an entry.")
        return

    with open("data.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        print("No entries found in the dictionary.")
    else:
        print("\nDictionary Report:")
        for line in lines:
            english_word, spanish_word = line.strip().split(',')
            print(f"{english_word} - {spanish_word}")

def takeQuiz():
    if not fileExists("data.txt"):
        print("Dictionary is empty. First add an entry.")
        return

    with open("data.txt", "r") as file:
        lines = file.readlines()

    if not lines:
        print("No entries available for the quiz.")
        return

    random.shuffle(lines)

    num_questions = min(5, len(lines))
    score = 0

    for i in range(num_questions):
        english_word, spanish_word = lines[i].strip().split(',')
        user_answer = input(f"What is the Spanish word for '{english_word}'? ")

        if user_answer.lower() == spanish_word.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is '{spanish_word}'.")

    print(f"\nYou scored {score} out of {num_questions}.")

while True:
    choice = mainMenu()
    if choice == "1":
        newEntry()
    elif choice == "2":
        translate()
    elif choice == "3":
        updateEntry()
    elif choice == "4":
        deleteEntry()
    elif choice == "5":
        produceReport()
    elif choice == "6":
        takeQuiz()
    elif choice == "7":
        print("Thanks for using the dictionary.")
        break
    else:
        print("Invalid choice. Please try again.")