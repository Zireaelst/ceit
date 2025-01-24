englishList = ["car"]
spanishList = ["coche"]

while True:
    print('''
        1) Add item to the dictionary
        2) Translate from English to Spanish
        3) Translate from Spanish to English
        4) Print the dictionary
        5) Delete an item
        6) Quit
    ''')

    number = input("Enter a number: ")

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
        while True:
            word = input("Enter the English word: ")
            if word in englishList:
                index = englishList.index(word)
                print("Spanish translation is:", spanishList[index])
                break
            else:
                print("This word is not in the dictionary.")
                print("Try another word.")

    elif number == "3":
        print("Available words for translation:", spanishList)
        while True:
            word = input("Enter the Spanish word: ")
            if word in spanishList:
                index = spanishList.index(word)
                print("English translation is:", englishList[index])
                break
            else:
                print("This word is not in the dictionary.")
                print("Try another word.")

    elif number == "4":
        print("Dictionary entries:")
        for eng, span in zip(englishList, spanishList):
            print(f"{eng} -> {span}")
        print("--------------------------------")

    elif number == "5":
        word = input("Enter the English or Spanish word to delete: ")
        if word in englishList:
            index = englishList.index(word)
            deleted_eng = englishList.pop(index)
            deleted_span = spanishList.pop(index)
            print(f"Deleted: {deleted_eng} -> {deleted_span}")
        elif word in spanishList:
            index = spanishList.index(word)
            deleted_span = spanishList.pop(index)
            deleted_eng = englishList.pop(index)
            print(f"Deleted: {deleted_eng} -> {deleted_span}")
        else:
            print("The translation is not found.")

    elif number == "6":
        print("QUITTING")
        break

    else:
        print("Please enter a valid option (1-6).")
