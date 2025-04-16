# Problem 1: Simulate rolling two dice, three times
import random

def roll_dice():
    for i in range(3):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"Roll {i + 1}: Die 1 = {die1}, Die 2 = {die2}")

# Problem 2: Mass-Energy Equivalence
def mass_energy_equivalence():
    C = 299792458  # Speed of light in m/s
    mass = float(input("Enter kilos of mass: "))
    energy = mass * C**2
    print(f"E = {mass} kg * {C}^2 = {energy} joules of energy!")

# Problem 3: Convert feet to inches
def feet_to_inches():
    feet = float(input("Enter feet: "))
    inches = feet * 12
    print(f"{feet} feet is equal to {inches} inches.")

# Problem 4: Calculate hypotenuse using the Pythagorean theorem
import math

def pythagorean_theorem():
    AB = float(input("Enter the length of AB: "))
    AC = float(input("Enter the length of AC: "))
    BC = math.sqrt(AB**2 + AC**2)
    print(f"The length of BC (the hypotenuse) is: {BC}")

# Problem 5: Division and remainder
def division_and_remainder():
    num1 = int(input("Please enter an integer to be divided: "))
    num2 = int(input("Please enter an integer to divide by: "))
    result = num1 // num2
    remainder = num1 % num2
    print(f"The result of this division is {result} with a remainder of {remainder}.")

# Problem 6: Calculate seconds in a year
def seconds_in_year():
    days_in_year = 365
    hours_in_day = 24
    minutes_in_hour = 60
    seconds_in_minute = 60
    seconds_in_a_year = days_in_year * hours_in_day * minutes_in_hour * seconds_in_minute
    print(f"There are {seconds_in_a_year} seconds in a year!")

# Problem 7: Mad Libs Game
def mad_libs():
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")
    print(f"Code in Place is fun. I learned to program and used Python to make my {adjective} {noun} {verb}!")

# Main function to run all programs
def main():
    roll_dice()
    mass_energy_equivalence()
    feet_to_inches()
    pythagorean_theorem()
    division_and_remainder()
    seconds_in_year()
    mad_libs()

if __name__ == "__main__":
    main()
