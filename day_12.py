# Question 44
# Write a program which can map() to make a list whose
# elements are square of numbers between 1 and 20 (both included).

lst = list(map(lambda x: x**2, range(1, 21)))
print("Question 44:")
print(lst)


# Question 45
# Define a class named American which has a static method called printNationality.

class American():
    @staticmethod
    def printNationality():
        print("American")


obj = American()
print("Question 45:")
obj.printNationality()


# Question 46
# Define a class named American and its subclass NewYorker.ˇ

class American2():
class NewYorker(American2):
