# - 2.2.1 Accepting User Input Using input()

""" 
    Build a script that requests three pieces of information from the user after the script runs.
    Collect name, birthdate and age.
"""

name = input("What is your name? ")
birthdate = input("When is your birthdate? ")
age = int(input("How old are you? "))

print(f"{name}, you are born on {birthdate}.")
print(f"Half of your age is { age/2 }.")