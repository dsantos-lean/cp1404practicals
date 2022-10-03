# 1.
out_file = open("name.txt", 'w')
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# 2.
in_file = open("name.txt")
name = in_file.read()
print(f"Your name is {name}")

# 3.
in_file = open("numbers.txt")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)

# 4.
in_file = open("numbers.txt")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
