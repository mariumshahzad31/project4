# 01. Sum of Two Numbers
def sum_two_numbers():
    print("Problem 01: Sum of Two Numbers")
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    total = first_number + second_number
    print("The sum of", first_number, "and", second_number, "is:", total)
    print()

# 02. Favorite Animal
def favorite_animal():
    print("Problem 02: Favorite Animal")
    animal = input("What's your favorite animal? ")
    print("My favorite animal is also", animal + "!")
    print()

# 03. Fahrenheit to Celsius
def fahrenheit_to_celsius():
    print("Problem 03: Fahrenheit to Celsius")
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print("Temperature:", str(fahrenheit) + "F =", str(celsius) + "C")
    print()

# 04. Age Riddle
def age_riddle():
    print("Problem 04: Age Riddle")
    anton = 21
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen
    print("Anton is", anton, "years old.")
    print("Beth is", beth, "years old.")
    print("Chen is", chen, "years old.")
    print("Drew is", drew, "years old.")
    print("Ethan is", ethan, "years old.")
    print()

# 05. Triangle Perimeter
def triangle_perimeter():
    print("Problem 05: Triangle Perimeter")
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))
    perimeter = side1 + side2 + side3
    print("The perimeter of the triangle is", perimeter)
    print()

# 06. Square of a Number
def square_number():
    print("Problem 06: Square of a Number")
    number = float(input("Type a number to see its square: "))
    square = number * number
    print(f"{number} squared is {square}")
    print()

# Run all problems in order
def main():
    sum_two_numbers()
    favorite_animal()
    fahrenheit_to_celsius()
    age_riddle()
    triangle_perimeter()
    square_number()

# Call main function
main()
