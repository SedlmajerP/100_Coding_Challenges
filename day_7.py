# Question 20
# Define a class with a generator which can iterate the numbers,
# which are divisible by 7, between a given range 0 and n.
# Suppose the following input is supplied to the program: 7
# Then, the output should be:
# 0
# 7

from math import sqrt
num = int(input())


class Generator():
    def counter(self, n):
        for i in range(0, n+1):
            if i % 7 == 0:
                yield i


gen = Generator()
generator = gen.counter(num)

for num in generator:
    print(num)

# Question 21
# A robot moves in a plane starting from the original point (0,0).
# The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps.
# The trace of robot movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps.
# Please write a program to compute the distance from current position after a sequence of movement and original point.
# If the distance is a float, then just print the nearest integer.
# Example: If the following tuples are given as input to the program:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# Then, the output of the program should be:
# 2

x1, x2 = 0, 0
y1, y2 = 0, 0

while True:
    seq_input = input().split()
    print(seq_input)
    if not seq_input:
        break
    if "UP" in seq_input:
        y1 += int(seq_input[1])
    if "DOWN" in seq_input:
        y2 += int(seq_input[1])
    if "LEFT" in seq_input:
        x2 += int(seq_input[1])
    if "RIGHT" in seq_input:
        x1 += int(seq_input[1])

dist = sqrt(((x1-x2)**2)+((y1-y2)**2))
print(int(dist))
