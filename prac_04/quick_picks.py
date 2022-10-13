import random

NUMBERS_PER_LINE = 6
MIN = 1
MAX = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick_lines = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MIN, MAX)
        while number in quick_pick_lines:
            number = random.randint(MIN, MAX)
        quick_pick_lines.append(number)
    quick_pick_lines.sort()
    print(" ".join(f"{number:2}" for number in quick_pick_lines))
