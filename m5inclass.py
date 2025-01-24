
englishList = ["car"]
spanishList = ["coche"]

while ...:
    print('''
        1) Add item to the dictionary
        2) Translate (English to Spanish) 
        3) Quit
    ''')
    number = input("Enter number:")

    if number == "1":
        while True:
            engWord = input("Enter English word: ")
            if engWord in englishList:
                print("English word is already in the dictionary.")
                print("Current English words:", englishList)
                print("Please enter an English word that isn't in the dictionary.")
            else:
                englishList.append(engWord)
                break

        while True:
            spanishWord = input("Enter the corresponding Spanish word: ")
            if spanishWord in spanishList:
                print("Spanish word is already in the dictionary.")
                print("Current Spanish words:", spanishList)
                print("Please enter a Spanish word that isn't in the dictionary.")
            else:
                spanishList.append(spanishWord)
                break

    elif number == "2":
        print("Available words for translation:", englishList)
        word = input("Write the English word you want to translate: ")
        if word in englishList:
            index = englishList.index(word)
            print("The Spanish translation is:", spanishList[index])
        else:
            print("This word is not in the dictionary.")

    elif number == "3":
        print("QUITTING")
        break

    else:
        print("Please enter a valid option (1, 2, or 3).")
