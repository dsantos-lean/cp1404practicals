import random


def main():
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    score = random.randint(1, 100)
    print(f"Random score is {score} = {result}")


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
