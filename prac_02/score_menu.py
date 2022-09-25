def main():
    score = ""
    print(f"(S)core (R)esult (P)rint stars (Q)uit")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "S":
            score = get_valid_score()
        elif choice == "R":
            result = determine_result(score)
            print(result)
        elif choice == "P":
            print_stars(score)
        else:
            print("Invalid choice")
        print(f"(S)core (R)esult (P)rint stars (Q)uit")
        choice = input(">>>").upper()
    print("Thank you for using the score menu.")


def get_valid_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(score):
    print("*" * score)


main()
