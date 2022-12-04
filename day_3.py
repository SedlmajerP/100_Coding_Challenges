# Question 10
# Write a program that accepts a sequence of whitespace separated words as input and
# prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

sentence = input().split(" ")
sorted_sentence = sorted(set(sentence))
for word in sorted_sentence:
    print(word, end=" ")


# Question 11
# Write a program which accepts a sequence of comma separated 4
# digit binary numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010
# Notes: Assume the data is input by console.

b_number = input().split(",")
lst = []
for n in b_number:
    if int(n, 2) % 5 == 0:
        lst.append(n)

print(",".join(lst))

# Question 12
# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number.The numbers obtained should be printed
# in a comma-separated sequence on a single line.

even_digits = []

for i in range(1000, 3001):
    even = 1
    for j in str(i):
        if int(j) % 2 != 0:
            even = 0
    if even == 1:
        even_digits.append(str(i))

print(",".join(even_digits))

# Question 13
# Write a program that accepts a sentence and calculate the number of letters and digits.

sentence1 = "hello world! 123"
letters, nums = 0, 0
for el in sentence1:
    if el.isdigit():
        nums += 1
    elif el.isalpha():
        letters += 1
print(f"LETTERS:{letters}\nDIGITS:{nums}")
