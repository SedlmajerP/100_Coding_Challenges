import timeit
import zlib
import random


# Question 75
# Please write a program to randomly print a integer number between 7 and 15 inclusive.


print("\nQuestion 75:")
print(random.randrange(7, 16))

# Question 76
# Please write a program to compress and decompress
# the string "hello world!hello world!hello world!hello world!".


string = "hello world!hello world!hello world!hello world!"
b_string = bytes(string, "utf-8")
comp = zlib.compress(b_string)
decomp = zlib.decompress(comp)
print(
    f"\nQuestion 76:\nString: {string}\nCompressed string: {comp}\nDecompressed string: {decomp}")


# Question 77
# Please write a program to print the running time of execution of "1+1" for 100 times.

print("\nQuestion 77:")
print(str(timeit.timeit("1+1", number=100)) + "s")

# Question 78
# Please write a program to shuffle and print the list [3,6,7,8].


lst = [3, 6, 7, 8]
random.shuffle(lst)

print("\nQuestion 78:")
print(lst)

# Question 79
# Please write a program to generate all sentences where subject is in ["I", "You"] and
# verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

subject = ["I", "You"]
verb = ["Play", "Love"]
object = ["Hockey", "Football"]


def sentences():
    for x in subject:
        for y in verb:
            for z in object:
                print(f"{x} {y} {z}")


print("\nQuestion 79:")
sentences()
