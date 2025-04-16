# 00. Check if a person is an adult
ADULT_AGE = 18

def is_adult(age):
    return age >= ADULT_AGE

# 01. Greet user
def greet(name):
    print(f"Greetings {name}!")

# 02. Check if number is in a range
def in_range(n, low, high):
    return low <= n <= high

# 03. Check fruit inventory
inventory = {
    'apple': 10,
    'banana': 25,
    'pear': 1000,
    'orange': 5
}

def num_in_stock(fruit):
    return inventory.get(fruit.lower(), 0)

# 04. Get user data
def get_user_data():
    first = input("What is your first name?: ")
    last = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first, last, email

# 05. Subtract seven from number
def subtract_seven(num):
    return num - 7

# MAIN FUNCTION
def main():
    # 00: Check adult
    age = int(input("How old is this person?: "))
    print(is_adult(age))

    # 01: Greet
    name = input("What's your name? ")
    greet(name)

    # 02: Range check
    print("\n--- Range Check ---")
    n = int(input("Enter a number to check: "))
    low = int(input("Enter low: "))
    high = int(input("Enter high: "))
    print("In range?" , in_range(n, low, high))

    # 03: Fruit inventory check
    print("\n--- Fruit Inventory ---")
    fruit = input("Enter a fruit: ")
    stock = num_in_stock(fruit)
    if stock > 0:
        print("This fruit is in stock! Here is how many:\n", stock)
    else:
        print("This fruit is not in stock.")

    # 04: Get and show user data
    print("\n--- User Data ---")
    user_data = get_user_data()
    print("Received the following user data:", user_data)

    # 05: Subtract seven
    print("\n--- Subtract Seven ---")
    number = int(input("Enter a number: "))
    print("Result after subtracting seven:", subtract_seven(number))

# Run main function
if __name__ == "__main__":
    main()
