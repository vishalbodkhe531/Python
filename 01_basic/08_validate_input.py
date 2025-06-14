user_input = int(input("Enter a number: "))

while not (0 < user_input <= 10):
    user_input = int(input("Enter again a number (between 1 and 10): "))

print("Done")