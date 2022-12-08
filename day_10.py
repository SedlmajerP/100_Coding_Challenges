# Question 31
# Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys.

def dict_def():
    dict = {i: i**2 for i in range(1, 21)}
    print(dict)


dict_def()

# Question 32
# Define a function which can generate a dictionary where the keys are numbers between
# 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.


def dict_gen():
    my_dict = {i: i**2 for i in range(1, 21)}
    for e in my_dict.keys():
        print(e, end=",")


dict_gen()

# Question 33
# Define a function which can generate and print a list where the values are square of
# numbers between 1 and 20 (both included).


def list_gen():
    lst = [num**2 for num in range(1, 21)]
    print(lst)


list_gen()


# Question 34
# Define a function which can generate a list where the values are square of numbers
#  between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

def lst_func1():
    my_lst = [i**2 for i in range(1, 21)]
    print(my_lst[0:5])


lst_func1()

# Question 35
# Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.


def lst_func2():
    my_lst2 = [i**2 for i in range(1, 21)]
    print(my_lst2[:-6:-1])


lst_func2()

# Question 36
# Define a function which can generate a list where the values are square of numbers
# between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.


def lst_func3():
    my_lst3 = [i**2 for i in range(1, 21)]
    print(my_lst3[5:])


lst_func3()


def tpl_func():
    my_tpl = tuple(n**2 for n in range(1, 21))
    print(my_tpl)


tpl_func()
