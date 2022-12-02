# QUESTION 4
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple
# which contains every number

# numbers = (input().split(","))


# def number_to_list_tuple(*args):
#     print(list(*args))
#     print(tuple(*args))


# number_to_list_tuple(numbers)

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
