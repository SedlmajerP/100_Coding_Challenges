# Question 38
# With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half
# values in one line and the last half values in one line.

tpl = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def divide_tpl(tpl):
    div = int(len(tpl)/2)
    print(tpl[:div])
    print(tpl[div:])


divide_tpl(tpl)


# Question 39
# Write a program to generate and print
# another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).


tpl2 = tuple(n for n in tpl if n % 2 == 0)
print(tpl2)

# Question 40
# Write a program which accepts a string as input to
# print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".ˇ

raw_str = input().casefold()

if raw_str == "yes":
    print("Yes")
else:
    print("No")

# Question 41
# Write a program which can map() to make a list whose elements are square
# of elements in [1,2,3,4,5,6,7,8,9,10].

lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst2 = map((lambda x: x**2), lst1)

print(list(lst2))


# Question 42
# Write a program which can map() and filter() to
# make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].


lst3 = list(map(lambda x: x**2, (list(filter(lambda x: x % 2 == 0, lst1)))))
print(lst3)

# Question 43
# Write a program which can filter() to make a list whose
# elements are even number between 1 and 20 (both included).

lst4 = list(filter(lambda x: x % 2 == 0, list(range(1, 21))))
print(lst4)
