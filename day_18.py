# Question 70
# Please write a program to output a random even number
# between 0 and 10 inclusive using random module and list comprehension.
import random

even_lst = [x for x in range(1, 11) if x % 2 == 0]
out = random.choice(even_lst)
print("\nQuestion 70:")
print(out)

# Question 71
# Please write a program to output a random number, which is divisible
# by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

lst = [x for x in range(10, 151) if x % 35 == 0]

print("\nQuestion71:")
print(random.choice(lst))

# Question 72
# Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.


lst1 = random.sample(range(100, 201), 5)
print("\nQustion 72:")
print(lst1)

# Question 73
# Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

print("\nQuestion 73:")
print(random.sample([x for x in range(100, 201) if x % 2 == 0], 5))

# Question 74
# Please write a program to randomly generate a list with 5 numbers,
# which are divisible by 5 and 7 , between 1 and 1000 inclusive.

print("\nQuestion 74:")
print(random.sample([x for x in range(1, 1001) if x % 35 == 0], 5))
