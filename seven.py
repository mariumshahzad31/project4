import random

# 00 - Average of two numbers
def average_of_two(num1, num2):
    return (num1 + num2) / 2

# 01 - Chaotic counting with random stopping
DONE_LIKELIHOOD = 0.3  # adjust this value as needed

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i, end=' ')

def main_chaotic():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

# 02 - Count even numbers from user input
def count_even():
    numbers = []
    while True:
        entry = input("Enter an integer or press enter to stop: ")
        if entry == "":
            break
        numbers.append(int(entry))
    even_count = sum(1 for num in numbers if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")

# 04 - Double a number
def double(num):
    return num * 2

def main_double():
    num = int(input("Enter a number: "))
    print(f"Double that is {double(num)}")

# 05 - Return your name
def get_name():
    return "Sophia"

def main_name():
    print(f"Howdy {get_name()} !")

# 06 - Print numbers 10 to 19, even/odd labels
def print_even_odd():
    for i in range(10, 20):
        label = "even" if i % 2 == 0 else "odd"
        print(f"{i} {label}", end=' ')
    print()

# 07 - Print all divisors of a number
def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')
    print()

def main_divisors():
    num = int(input("Enter a number: "))
    print_divisors(num)

# 08 - Print a message multiple times
def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main_print_multiple():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

# 09 - Make sentence from word and part of speech
def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")
    else:
        print("Invalid part of speech.")

def main_make_sentence():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

# 10 - Print the one's digit
def print_ones_digit(num):
    print(f"The ones digit is {num % 10}")

def main_ones_digit():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

