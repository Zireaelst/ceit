import random

print("Word Prediction Game")
word_list = ["RECURSION", "ITERATION", 'CONDITIONS', 'PROGRAMMING', 'VARIABLES']
word = random.choice(word_list)
# to print the word to be guesses in this format ________
unknown = len(word) * '_'
print(unknown)
points = 12
guesses_left = 3
letters_purchased = 0
max_letter_purchases = 4
print("__ __ __ _ __")
print("the word has",len(word),"letters")
print("You have 12 points in total to start with.")
print("You can buy a letter at a cost of 2 points.")
print("You can buy 4 letters at max.")
print("You can make a guess at max 3 times.")
print("Each wrong guess results in 2-point loss.")

while True:
    op = int(input("1. Make a guess \n 2. Buy a letter \n What do to:"))
    if op == 1:
        if guesses_left > 0:
            guess = input("Make your guess: ").strip().upper()
            if guess == word:
                print(word, "*** Congrats, you won! ***")
                break
            else:
                guesses_left -= 1
                points -= 2
                print("Incorrect guess!")
                print("***Remaining points:", points, "***")
        else:
            print("No guesses left! The game ended.")
            print("The answer is", word)
            break
    elif op == 2:
        if letters_purchased >= max_letter_purchases:
            print("You cannot buy more letters. You have already purchased 4 letters.")
        elif points < 2:
            print("Not enough points to buy a letter.")
        else:
            points -= 2
            letters_purchased += 1
            while True:
                unknown = list(unknown)
                random_index = random.randint(0, len(word) - 1)
                if unknown[random_index] == '_':
                    unknown[random_index] = word[random_index]
                    unknown = '' .join(unknown)
                    break
            print("The letter purchased is:", word[random_index])
            print("Current Word State:", unknown)


    elif "_" not in unknown:
        print(word, "*** Congrats, you won! ***")
        break
    elif points <= 0 or guesses_left <= 0:
        print("The game ended.")
        print("No points left or you finished your guesses.")
        print("The answer is", word)
        break
