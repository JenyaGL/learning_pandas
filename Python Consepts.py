# there are basic concepts in python
#----------------
# variables:
user_name = 'jack' # string
age = 35 # integer
volume = 100 # integer
limit = 10.5 # float
active = False # boolean
items = ['item1', 'item2', 'item3'] # list
user_info = {'name': user_name, 'age': age} # dictionary
coordinates = (10.0, 20.0) # tuple

# Input and Output (the ask)

campaign = input("Enter campaign name: ")
print("Campaign name is:", campaign)

# input command will always return as string, if we need to do math we have to use this:

# Casting: (the fix)

budget = input("Enter budget: ")
budget_number = int(budget)  # casting string to integer

# f-strings (The Display):
print(f"User {user_name} is {age} years old and has a budget of {budget_number}.")



#--------------------


# Exercise 1: Calculate how many months a user has been alive

# 1. Ask for name
name = input("What is your name? ")

# 2. Ask for age
age_text = input("How old are you? ")

# 3. Convert age to a number (integer)
age_number = int(age_text)

# 4. Do the math (Calculate months)
months_alive = age_number * 12 # <--- You fill this in

# 5. Print the result using an f-string
print(f"Wow {name}, you have been alive for {months_alive} months!")


#--------------------

# Logic flow: if statements

# The Concepts

# The if statement: Checks if something is True.
# The else statement: What to do if it's False.
# Comparison Operators:
# > (Greater than)
# < (Less than)
# == (Equal to - Note the double equals!)
# >= (Greater or equal)
# <= (Less or equal)
# != (Not equal)

# If statements build on indentation
cpm = 10

if cpm > 10:
    print("This is a cpm.")
else:
    print("This is not a cpm.")

# Assignment 2: The "Budget Guard"

# 1. Ask for CPM
cpm_text = input("whats the CPM? ")

# 2. Convert age to a number (integer)
cpm_number = int(cpm_text)

if cpm_number == 0:                                 # catching errors should be first!
    print("value is 0, check the settings/tracking")
elif cpm_number > 20:                               # then high cost
    print("High Cost! Alert Manager.")
elif cpm_number <= 5:                               # then low cost
    print("Low Cost! Buy more.")
else:                                               # then standard cost
    print("Standard pricing")


#--------------------
# The Power of Loops

