# def countdown(n):
#     if n <= 0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n - 1)

number = int(input("Enter the number: "))

# countdown(number)


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(number))