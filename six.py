# 00 - Guess My Number 
print("\n=== 00 - Guess My Number ===")
secret_number = int(input("Set the secret number (0-99) for guessing: "))
print("\nNow pass the keyboard to the guesser!\n")
print("I am thinking of a number between 0 and 99...")

guess = int(input("Enter a guess: "))
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    guess = int(input("Enter a new number: "))
print(f"Congrats! The number was: {secret_number}.")

# ----------------------------------------------

# 01 - Fibonacci Sequence up to 10,000
print("\n\n=== 01 - Fibonacci Sequence (Up to 10,000) ===")
MAX_VALUE = 10000
a, b = 0, 1
while a < MAX_VALUE:
    print(a, end=' ')
    a, b = b, a + b
print()

# ----------------------------------------------

# 02 - First 20 Even Numbers
print("\n\n=== 02 - First 20 Even Numbers ===")
count = 0
even = 0
while count < 20:
    print(even, end=' ')
    even += 2
    count += 1
print()

# ----------------------------------------------

# 03 - Affirmation Until Correct
print("\n\n=== 03 - Affirmation Until Correct ===")
affirmation = "I am capable of doing anything I put my mind to."
print(f"Please type the following affirmation:\n{affirmation}")
while True:
    user_input = input()
    if user_input == affirmation:
        print("That's right! :)")
        break
    else:
        print("Hmmm That was not the affirmation. Please try again:")

# ----------------------------------------------

# 04 - Spaceship Countdown
print("\n\n=== 04 - Spaceship Countdown ===")
for i in range(10, 0, -1):
    print(i, end=' ')
print("Liftoff!")

# ----------------------------------------------

# 05 - Double Until 100 or More
print("\n\n=== 05 - Double the Number Until >= 100 ===")
curr_value = int(input("Enter a number to start doubling: "))
while curr_value < 100:
    curr_value *= 2
    print(curr_value, end=' ')
print()
