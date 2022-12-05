# Question 16
# Use a list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

list_input = input().split(",")
squared_odd = [str(int(n)**2) for n in list_input if int(n) % 2 != 0]
print(",".join(squared_odd))

# Question 17
# Write a program that computes the net amount of a bank account based a transaction log from console input.
# The transaction log format is shown as following:
# D 100
# W 200
# D means deposit while W means withdrawal.

deposit, withdrawl = 0, 0
while True:
    acc = input().split()
    print(acc, len(acc))
    if "D" in acc:
        for e in acc:
            if e.isnumeric():
                deposit += int(e)
    elif "W" in acc:
        for e in acc:
            if e.isnumeric():
                withdrawl += int(e)
    if len(acc) == 0:
        break

print(f"Account balance is: {deposit - withdrawl}")
