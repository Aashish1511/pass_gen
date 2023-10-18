#password generator using random method
"""import random

print("Welcome to your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = input("Enter the Amount of Password to generate: ")
number = int(number)


length = input("Tell us Your Password length: ")
length = int(length)

print("\nHere are your passwords: ")

for pwd in range (number):
    password = " "
    for c in range(length):
        password += random.choice(chars)
    print(password)"""

#above code is as same as using Random method 
import random

print("Welcome to your Password Generator")

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = int(input("Enter the Amount of Password to generate: "))
#number = int(number)


length = int(input("Tell us Your Password length: "))
#length = int(length)

print("\nHere are your passwords: ")

for pwd in range (number):
    password = " "
    for c in range(length):
        password += random.choice(chars)
    print(password)