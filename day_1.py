# QUESTION 1
# Write a program which will find all such numbers which are divisible by 7 but are
# not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line

for number in range(2000, 3201):
    if number % 7 == 0 and number % 5 != 0:
        print(number, end=",")


# QUESTION 2
# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be:40320

num = int(input())


def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    return fact


print(factorial(num))

# QUESTION 3
# With a given integral number n, write a program to generate a dictionary that contains (i, i x i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.


def func(num):
    mydict = {}
    for i in range(1, num+1):
        mydict[i] = i*i
    return(mydict)


print(func(num))
