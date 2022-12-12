# Question 60
# Write a program to compute:
# f(n)=f(n-1)+100 when n>0
# and f(0)=0
# with a given n input by console (n>0).
# Example: If the following n is given as input to the program: 5
# Then, the output of the program should be: 500


def recurs(n):
    if (n > 0):
        result = recurs(n-1) + 100
    else:
        result = 0
    return result


print("\nQustion 60:\nEnter a number > 0:")
num = int(input())
print(recurs(num))


# Question 61
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: If the following n is given as input to the program: 7
# Then, the output of the program should be: 13

def fib(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib(n-1) + fib(n-2)
    return res


print("\nQuestion 61:\nEnter a positive number:")
fib_input = int(input())
print(fib(fib_input))


# Question 62
# The Fibonacci Sequence is computed based on the following formula:
# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1
# Please write a program to compute the value of f(n) with a given n input by console.
# Example: If the following n is given as input to the program: 7
# Then, the output of the program should be: 0,1,1,2,3,5,8,13

def fib2(n):
    if n == 0:
        res = 0
    elif n == 1:
        res = 1
    else:
        res = fib2(n-1) + fib2(n-2)
    return res


print("\nQustion 62:\nEnter a positive number:")
n = int(input())

out = [str(fib2(x)) for x in range(0, n+1)]
print(",".join(out))

# Question 63
# Please write a program using generator to print the even numbers
# between 0 and n in comma separated form while n is input by console.
# Example: If the following n is given as input to the program: 10
# Then, the output of the program should be: 0,2,4,6,8,10


def evenGen(num):
    i = 0
    while i < num:
        if i % 2 == 0:
            yield i
        i += 1


print("\nQuestion 63:\nEnter a number:")
num = int(input())
out = [str(n) for n in evenGen(num)]
print(",".join(out))

# Question 64
# Please write a program using generator to print the numbers which can be
# divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.
# Example: If the following n is given as input to the program: 100
# Then, the output of the program should be: 0,35,70
# In case of input data being supplied to the question, it should be assumed to be a console input.


def div_5_7(n):
    for i in range(0, n+1):
        if i % 35 == 0:
            yield i


print("\nQuestion 64:\nEnter a number > 35:")
num2 = int(input())
ans = [str(n) for n in div_5_7(num2)]
print(",".join(ans))
