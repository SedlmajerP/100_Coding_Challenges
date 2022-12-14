# Question 26
# Define a function which can compute the sum of two numbers.


def my_sum(n1, n2): return n1+n2


print(my_sum(2, 5))


# Question 27
# Define a function that can convert a integer into a string and print it in console.


def convert(x): return str(x)


print(convert(8))


# Question 28
# Define a function that can receive two integer numbers in string form
# and compute their sum and then print it in console.


def sum(x1, x2): return int(x1)+int(x2)


print(sum("2", "8"))


# Question 29
# Define a function that can accept two strings as input and concatenate them and then print it in console.

def conc(w1, w2): return w1+w2


print(conc("hello", " world"))


# Question 30
# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print all strings line by line.

def compare(str1, str2):
    if len(str1) < len(str2):
        return str2
    elif len(str1) == len(str2):
        return(f"{str1}\n{str2}")
    else:
        return(str1)


print(compare("hello", "world"))
