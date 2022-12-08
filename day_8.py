# Question 22
# Write a program to compute the frequency of the words from the input.
# The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.


sentence = input().split()
lst = []
for w in sentence:
    x = (f"{w}:{sentence.count(w)}")
    lst.append(x)
sorted = sorted(lst)
for e in sorted:
    print(e)


# Question 23
# Write a method which can calculate square value of number


class MyClass:
    def squared(self, num):
        print(num**2)


my_math = MyClass()
my_math.squared(7)


# Question 24
# Python has many built-in functions, and if you do not know how to use it,
# you can read document online or find some books.
# But Python has a built-in document function for every built-in functions.
# Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()
# And add document for your own function


def doc(int):
    """Fuction that returns square number.

    parameter must be an integer
    """
    return (int**2)


help(range)
help(doc)


# Question 25
# Define a class, which have a class parameter and have a same instance parameter.
# Hints:
# Define an instance parameter, need add it in __init__ method.
# You can init an object with construct parameter or set the value later


class User():
    name = "User"

    def __init__(self, name=None):
        self.name = name


john = User("John")
print(User.name, john.name, )
david = User()
david.name = "David"
print(User.name, david.name)
