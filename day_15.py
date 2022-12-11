# Question 54
# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the company name of a given email address.
# Both user names and company names are composed of letters only.
# Example: If the following email address is given as input to the program: john@google.com
# Then, the output of the program should be: google

import re

print("\nQuastion 54:\nEnter an email:")

email = input()
pattern = r"\w+@(\w+).com"
company = re.findall(pattern, email)
print(",".join(company))

# Question 55
# Write a program which accepts a sequence of words separated by whitespace as input
# to print the words composed of digits only.
# Example: If the following words is given as input to the program: 2 cats and 3 dogs.
# Then, the output of the program should be: ['2', '3']

print("\nQuestion 55:\nEnter sequence of words and digits separated with whitespace:")
seq = input().split()
out = [e for e in seq if e.isnumeric()]
print(out)


# Question 56
# Print a unicode string "hello world".
print("\nQustion 56:")
print(u"hello world")

# Question 57
# Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.


def converter(string):
    out = string.encode("utf-8")
    print(out)


print("\nQuestion 57:")
converter("Mé jméno je Pavel a příjmení Sedlmajer")

# Question 58
# Write a special comment to indicate a Python source code file is in unicode.

# -*- coding: utf-8 -*-


# Question 59
# Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5
# Then, the output of the program should be: 3.55ˇ

print("\nQustion 59:\nEnter a number:")
n = int(input())


def count(n):
    x = 0
    for i in range(1, n+1):
        x += i/(i+1)
    print(x)


count(n)
