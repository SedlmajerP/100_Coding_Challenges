# Question 18
# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12

# Your program should accept a sequence of comma separated passwords and
# will check them according to the above criteria.
# Passwords that match the criteria are to be printed, each separated by a comma.

import re
pass_sequence = input().split(",")
print(pass_sequence)
lst = []
for e in pass_sequence:
    if 12 >= len(e) >= 6 and re.search(r"[a-zA-Z0-9][$#@]\S", e):
        lst.append(e)
print(",".join(lst))

# Question 19

# You are required to write a program to sort the (name, age, score) tuples by ascending order
# where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name
# 2: Then sort based on age
# 3: Then sort by score
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


lst = []
while True:
    player = input().split(",")
    if not player[0]:
        break
    lst.append(tuple(player))

lst.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))
print(lst)
