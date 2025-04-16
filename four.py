import random

# 01: Program that prints the first 20 even numbers
def print_even_numbers():
    print("First 20 even numbers:")
    for i in range(0, 40, 2):  # start at 0, go up to 40 (exclusive), step by 2
        print(i, end=" ")
    print()  # for newline

# 02: Program to check voting eligibility in fictional countries
def voting_eligibility():
    age = int(input("How old are you? "))
    print("Voting eligibility:")
    
    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")
        
    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")
        
    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

# 03: Program to check if a year is a leap year
def check_leap_year():
    year = int(input("Enter a year: "))
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

# 04: Program to check if the user is tall enough for a ride
def check_height():
    while True:
        height = input("How tall are you? ")
        if height == "":
            break  # exit if no height is entered
        height = int(height)
        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

# 05: Program to print 10 random numbers in the range 1 to 100
def print_random_numbers():
    print("10 random numbers between 1 and 100:")
    for _ in range(10):
        print(random.randint(1, 100), end=" ")
    print()  # for newline

# Main function to run all tasks
def main():
    print_even_numbers()
    voting_eligibility()
    check_leap_year()
    check_height()
    print_random_numbers()

if __name__ == "__main__":
    main()
