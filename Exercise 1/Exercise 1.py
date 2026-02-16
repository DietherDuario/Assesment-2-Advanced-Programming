import random

def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    while True:
        try:
            choice = int(input("Choose your difficulty (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter a valid number (1-3).")
        except ValueError:
            print("Invalid input. Please enter a number.")
def randomInt(level):
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(1000, 9999)
def decideOperation():
    return random.choice(['+', '-'])
def displayProblem(num1, num2, op):
    print(f"\n{num1} {op} {num2} = ", end="")
    while True:
        try:
            answer = int(input())
            return answer
        except ValueError:
            print("Please enter a valid integer: ", end="")
def isCorrect(num1, num2, op, user_answer):
    if op == '+':
        return user_answer == (num1 + num2)
    else:
        return user_answer == (num1 - num2)

def displayResults(score):
    print("\n------------------------------")
    print(f"Your final score is: {score}/100")
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    print(f"Your grade: {grade}")
    print("------------------------------")

def main():
    print("Welcome to the Arithmetic Quiz!")

    while True:
        level = displayMenu()
        score = 0

        for i in range(1, 11):
            num1 = randomInt(level)
            num2 = randomInt(level)
            op = decideOperation()

            print(f"\nQuestion {i}:")
            user_answer = displayProblem(num1, num2, op)

            if isCorrect(num1, num2, op, user_answer):
                print("Correct! (+10 points)")
                score += 10
            else:
                print("Incorrect. Try again!")
                user_answer = displayProblem(num1, num2, op)
                if isCorrect(num1, num2, op, user_answer):
                    print("Correct on second try! (+5 points)")
                    score += 5
                else:
                    print("Wrong again. No points.")
        displayResults(score)
        again = input("Would you like to play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing! Goodbye!")
            break
if __name__ == "__main__":
    main()
