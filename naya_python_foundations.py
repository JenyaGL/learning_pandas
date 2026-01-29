# ex 1
# declare new variable that will hold your first name, print out your name
first_name = "Jenya"

print(first_name)

# ex 2
#Change the print so it will print each value in seperate line
print('hello','world','pizza', sep='\n' , end='\n')


# ex 3
#ask the user for first name and last name print each in different line
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")

print(first_name, last_name, sep=' ', end='\n')

# ex 4
#assign value to 2 numbers:
this_year = 2026
birth_year = 1994

my_age = this_year - birth_year

print("My age is: " + str(my_age))


# ex 5
#Create variables a = "100" and b = 25.
#Convert a to an integer and add it to b.
#Print the result and its type.

a= "100"
b= 25

result= int(a) + b
print(result,type(result))


# ex 6
# For each value below, predict bool(value) before running the code:
values =[0,"","0",None,[],[0]]



# ex 7
#Compute the number of full minutes and remaining seconds in total_seconds = 367.
#Store them in minutes and seconds.


#-------------------------

import random

# The computer "chooses" a number
secret = random.randint(1, 100)

print("I have chosen a number between 1 and 100.")
print("Try to guess it...")

guess = int(input("Your guess: "))

# Game loop. Keep on going until guess matches secret
while guess != secret:
    # User feedback
    if guess > secret:
        print("Too high, try again...")
    else:
        print("Too low, try again...")
    guess = int(input("Your guess: "))

print("Nice! GAME OVER")

#-----------------------

import pandas as pd
import seaborn as sns

df = pd.read_csv("diamonds.csv")

df.head()

# Filter rows (carat > 2.5 and price < 10000)
df[(df.carat > 2.5) & (df.price < 10000)]

# Average price per cut
print(df.groupby("cut")["price"].mean().sort_values())

# Simple visualization
print(sns.boxplot(x="clarity", y="price", data=df))


