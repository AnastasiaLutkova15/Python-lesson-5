# Task 26

A = int(input("Введите число: "))
B = int(input("Введите степень: "))
def power(A, B):
    if B == 0:
        return 1
    return power(A, B - 1) * A
print(power(A, B))

# Task 28

# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))
# def sum(a, b):
#     if a == 0:
#         return b
#     else:
#         return sum(a - 1, b + 1)
# print(sum(a, b))



