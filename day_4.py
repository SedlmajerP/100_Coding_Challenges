# Question 14
# Write a program that accepts a sentence and calculate
# the number of upper case letters and lower case letters.

# sentence = input("Enter a sentence:")
# upper, lower = 0, 0
# for e in sentence:
#     if e.isupper():
#         upper += 1
#     elif e.islower():
#         lower += 1
# print(f"UPPER:{upper}\nLOWER:{lower}")

# Question 15
# Write a program that computes the value of a+aa+aaa+aaaa
# with a given digit as the value of a.

digit = input()


def calc(a):
    out = int(a)+int(2*a)+int(3*a)+int(4*a)
    print(out)


calc(digit)
