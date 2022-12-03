# # QUESTION 4
# # Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# # which contains every number

from math import sqrt
numbers = (input().split(","))


def number_to_list_tuple(*args):
    print(list(*args))
    print(tuple(*args))


number_to_list_tuple(numbers)

# # Question 5
# # Define a class which has at least two methods:
# # getString: to get a string from console input
# # printString: to print the string in upper case.
# # Also please include simple test function to test the class methods.


class GetStringPrintString:
    def get_string():
        message = input()
        return message.upper()

    def print_string():
        print(GetStringPrintString.get_string())


instantiate = GetStringPrintString

instantiate.print_string()

# Question 6
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 _ C _ D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# For example Let us assume the following comma separated input sequence is given to the program: 100,150,180
# The output of the program should be: 18,22,24


c = 50
h = 30
inputs = input().split(sep=",")


def formula(nums):
    for num in nums:
        q = sqrt((2*c*int(num))/h)
        print(int(q), end=",")


formula(inputs)


# Question 7
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i _ j.*
# Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

inputs = input().split(",")
X = int(inputs[0])
Y = int(inputs[1])

arr = [[i*j for j in range(Y)] for i in range(X)]
print(arr)

# Question 8
# Write a program that accepts a comma separated sequence of words as input and prints the words
# in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

inputs = sorted(input().split(","))
for word in inputs:
    print(word, end=",")


# Question 9
# Write a program that accepts sequence of lines as input and prints the lines after making
# all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

my_list = []
while True:
    sentence = input()
    my_list.append(sentence.upper())
    if len(sentence) == 0:
        break
for line in my_list:
    print(line)
