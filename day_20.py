# Question 80
# Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

import pprint
lst = [5, 6, 77, 45, 22, 12, 24]
odd_lst = list(filter(lambda x: x % 2 != 0, lst))
print(f"\nQuestion 80:\n{odd_lst}")


# Question 81
# By using list comprehension, please write a program to print the list after
# removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

lst1 = [12, 24, 35, 70, 88, 120, 155]
odd_lst1 = [x for x in lst1 if x % 35 != 0]
print(f"\nQuestion 81:\n{odd_lst1}")

# Question 82
# By using list comprehension, please write a program to print the list
# after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

lst2 = [12, 24, 35, 70, 88, 120, 155]
lst2_rem = [x for i, x in enumerate(lst2) if i % 2 == 0]
# for x, i in enumerate(lst2):
#     if x % 2 == 0:
#         lst2_rem.append(i)
print(f"\nQuestion 82:\n{lst2_rem}")

# Question 83
# By using list comprehension, please write a program to print the list
# after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].ˇ

lst3 = [12, 24, 35, 70, 88, 120, 155]
lst3_rem = [x for i, x in enumerate(lst3) if i not in range(1, 5)]

print(f"\nQuestion 83:\n{lst3_rem}")

# Question 84
# By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

arr_3d = [[[0 for x in range(3)] for y in range(5)] for z in range(8)]
print("\nQuestion 84:")
pprint.pprint(arr_3d)
