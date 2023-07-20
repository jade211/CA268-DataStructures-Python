#!/usr/bin/env python3

# QUESTION 1 - Worked on by Jade Hudson and Sruthi Santhosh
def sum_q1(n):
    if n <= 0:
        return n
    else :
        return n + sum_q1(n - 1)


print(sum_q1(6))



# QUESTION 2 - Worked on by Jade Hudson and Sruthi Santhosh
def int_reverse(n):
    n = str(n)
    if len(n) == 0:
        return n
    else:
        return int_reverse(n[1:]) + n[0]


print(int_reverse(123))



# QUESTION 3 - Worked on by Jade Hudson and Sruthi Santhosh
def str_reverse(n):
    if len(n) == 0:
        return n
    else:
        return str_reverse(n[1:]) + n[0]


print(str_reverse("hello"))



# QUESTION 4
def inverse(lst):
    if len(lst) == 0:
        return []
    else:
        return [lst[-1]] + inverse(lst[:-1])


print(inverse([1, 2, 3, 4]))



# QUESTION 5 *****
def multiply(num1, num2):
    if num2 == 0 or num1 == 0:
        return 0
    elif num2 < 0:
        return - num1 + multiply(num1, num2 + 1)
    else:
        return num1 + multiply(num1, num2 - 1)


print(multiply(10, 2))
print(multiply(-51, -4))
print(multiply(3, 9))



# QUESTION 6
def is_heteromecic(n):
    i = 0
    while i <= (n ** (1 / 2)):
        if n == i * (i + 1):
            return True
        i = i + 1  # Will return False if True is not reached within the loop
    return False


print(is_heteromecic(120))



# QUESTION 7
def length(s):
    if len(s) == 0:
        return 0
    else:
        return length(s[:len(s) - 1]) + 1


print(length("hello"))
