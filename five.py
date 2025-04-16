import hashlib

# Question 1: Function for counting occurrences of numbers in a list
def count_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to stop): ")
        if user_input == 'done':
            break
        else:
            try:
                number = int(user_input)
                numbers.append(number)
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    # Count the occurrences using a dictionary
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    
    # Display the result
    for number, count in count_dict.items():
        print(f"{number} appears {count} times.")

# Question 2: Function for calculating total cost of fruits
def fruit_shop():
    fruit_prices = {
        'apple': 1.5,
        'durian': 3.0,
        'jackfruit': 2.5,
        'kiwi': 2.0,
        'rambutan': 4.0,
        'mango': 2.5
    }

    total_cost = 0
    for fruit, price in fruit_prices.items():
        quantity = input(f"How many ({fruit}) do you want?: ")
        try:
            quantity = int(quantity)
            total_cost += quantity * price
        except ValueError:
            print(f"Invalid input for {fruit}, assuming 0.")
    
    print(f"Your total is ${total_cost:.2f}.")

# Question 3: Function for password hashing and login simulation
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    stored_logins = {
        'user1@example.com': '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824',  # Hash for 'hello'
    }

    email = input("Enter email: ")
    password = input("Enter password: ")
    
    if email in stored_logins:
        stored_hash = stored_logins[email]
        password_hash = hash_password(password)
        if stored_hash == password_hash:
            print("Login successful.")
        else:
            print("Login failed.")
    else:
        print("Email not found.")

# Main program menu
def main():
    print("Choose a program to run:")
    print("1. Count occurrences of numbers in a list (Question 1)")
    print("2. Fruit shop cost calculator (Question 2)")
    print("3. Password hashing and login (Question 3)")
    
    choice = input("Enter the number of your choice: ")

    if choice == '1':
        count_numbers()
    elif choice == '2':
        fruit_shop()
    elif choice == '3':
        login()
    else:
        print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
