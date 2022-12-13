# Question 65
# Please write assert statements to verify that every number in the list [2,4,6,8] is even

# even_lst = [2, 4, 6, 8]

# for i in even_lst:
#     assert i % 2 == 0, f"{i} is not an even number"


# Question 66
# Please write a program which accepts basic mathematic
# expression from console and print the evaluation result.

# x = input()
# print(eval(x))


# Question 67
# Please write a binary search function which searches an item in a sorted list.
# The function should return the index of element to be searched in the list.

import random
lst = [1, 5, 8, 10, 12, 13, 55, 66, 73, 78, 82, 85, 88, 99]


def bi_serach(lst, num_to_look):
    low = 0
    high = len(lst)
    while low <= high:
        middle = round((low+high)//2)
        if lst[middle] == num_to_look:
            return middle
        elif lst[middle] < num_to_look:
            low = middle + 1
        else:
            high = middle - 1
    return -1


index = int(bi_serach(lst, 55))
if index >= 0:
    print(f"\nQustion 67:\nThe number you are lookng for is at index: {index}")
else:
    print("number not in list")

# Question 68
# Please generate a random float where the value is between 10 and 100 using Python module.


x = random.uniform(10, 100)
print("\nQuestion 68:")
print(x)

# Question 69
# Please generate a random float where the value is between 5 and 95 using Python module.

rng_float = random.uniform(5, 95)
print(f"\nQuestion 69:\n{x}")
