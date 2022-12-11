# Question 51
# Write a function to compute 5/0 and use try/except to catch the exceptions.

import re


def div(x, y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print("Cannot divide by 0")


print("\nQuestion 51:")
div(5, 0)

# Question 52
# Define a custom exception class which takes a string message as attribute.


class CustomExeption(Exception):
    """This is Custom Exception 

    Atributes:
    message = explanation of the error
    """

    def __init__(self, message):
        self.message = message


print("\nQuestion 52:\nEnter a number")

num = int(input())
try:
    if num < 10:
        raise CustomExeption("Number is lower than 10")
    if num > 10:
        raise CustomExeption("Number is greater than 10")
except CustomExeption as ce:
    print("Raised error: " + ce.message)

# Question 53
# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address. Both user names and
# company names are composed of letters only.
# Example: If the following email address is given as input to the program: john@google.com
# Then, the output of the program should be: john


print("\nQustion 53:\nEnter email adress:")
mail = input()
pattern = r"(\w+)@\w+.com"
name = re.findall(pattern, mail)
print(",".join(name))
