import os

def mainMenu():
    print("\nQuiz Score Tracker")
    print("1. Record Quiz Score")
    print("2. Generate Report")
    print("3. Find Student Score")
    print("4. Exit")
    return input("Enter your choice: ")

def recordQuizScore():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    score = input("Enter quiz score: ")
    with open("quiz_scores.txt", "a") as file:
        file.write(f"{student_id},{name},{score}\n")
    print("Score recorded successfully!")

def generateReport():
    if not os.path.exists("quiz_scores.txt"):
        print("File does not exist. First record some quiz data.")
        return

    scores = []
    with open("quiz_scores.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3:
                scores.append(float(parts[2]))

    if scores:
        print(f"Average quiz score: {sum(scores)/len(scores):.1f}")
        print(f"Highest quiz score: {max(scores):.1f}")
        print(f"Lowest quiz score: {min(scores):.1f}")
    else:
        print("No quiz data available.")

def findStudentScore():
    if not os.path.exists("quiz_scores.txt"):
        print("File does not exist. First record some quiz data.")
        return

    student_id = input("Enter the student ID to search for: ")
    with open("quiz_scores.txt", "r") as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) == 3 and parts[0] == student_id:
                print(f"Score for student ID {student_id}: {parts[2]}")
                return
    print(f"No score found for student ID {student_id}.")

def main():
    while True:
        choice = mainMenu()
        if choice == "1":
            recordQuizScore()
        elif choice == "2":
            generateReport()
        elif choice == "3":
            findStudentScore()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
